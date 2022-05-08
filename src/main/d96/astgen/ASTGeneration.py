# from D96Visitor import D96Visitor
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

from functools import reduce


def flatten(lst):
    return reduce(lambda x, y: x + y, lst, [])


def text2float(text):
    if text[0] == '.' and (text[1] == 'e' or text[1] == 'E'):
        return float('0' + text)
    return float(text)


def text2int(text):
    if text[0] != '0':
        return int(text)
    elif text == '0':
        return 0
    elif text[1] in ['x', 'X']:
        return int(text, 16)
    elif text[1] in ['b', 'B']:
        return int(text, 2)
    return int(text[0] + 'o' + text[1:], 8)


class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        a = [self.visit(i) for i in ctx.class_decl()]
        # a = flatten(a)
        return Program(a)

    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        return self.visit(ctx.class_type())

    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.class_block())
        memlist = flatten(memlist)
        parentname: Id = None
        if ctx.ID(1):
            parentname = Id(ctx.ID(1).getText())
        # TODO: Check static main instance
        return ClassDecl(classname, memlist, parentname)

    # Visit a parse tree produced by D96Parser#class_block.
    def visitClass_block(self, ctx: D96Parser.Class_blockContext):
        return [self.visit(i) for i in ctx.class_stmt()]

    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx: D96Parser.Class_stmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        if ctx.VAL():  # TODO: Check declare null classtype
            if ctx.attr_decl_1():
                idList, type_ = self.visit(ctx.attr_decl_1())
                return [AttributeDecl(Static(), ConstDecl(i, type_)) if '$' in str(i) else AttributeDecl(Instance(),
                                                                                                         ConstDecl(i,
                                                                                                                   type_))
                        for i in idList]
            lst1, lst2, type_ = self.visit(ctx.attr_decl_2())
            length = len(lst1)
            lst1.reverse()
            # ret = [(Id("a"), 2), IntType]
            return [
                AttributeDecl(Static(), ConstDecl(lst1[i], type_, lst2[i])) if '$' in str(lst1[i]) else AttributeDecl(
                    Instance(), ConstDecl(lst1[i], type_, lst2[i])) for i in range(length)]

        # Variable
        if ctx.attr_decl_1():
            idList, type_ = self.visit(ctx.attr_decl_1())
            if "Id(" in str(type_):
                return [AttributeDecl(Static(), VarDecl(i, type_, NullLiteral())) if '$' in str(i) else AttributeDecl(
                    Instance(), VarDecl(i, type_, NullLiteral())) for i in idList]
            return [AttributeDecl(Static(), VarDecl(i, type_)) if '$' in str(i) else AttributeDecl(Instance(),
                                                                                                   VarDecl(i, type_))
                    for i in idList]
        lst1, lst2, type_ = self.visit(ctx.attr_decl_2())
        length = len(lst1)
        lst1.reverse()
        # ret = [(Id("a"), 2), IntType]
        return [AttributeDecl(Static(), VarDecl(lst1[i], type_, lst2[i])) if '$' in str(lst1[i]) else AttributeDecl(
            Instance(), VarDecl(lst1[i], type_, lst2[i])) for i in range(length)]

    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        kind = Static()
        param = []
        if ctx.list_param():
            param = self.visit(ctx.list_param())
        body = self.visit(ctx.stmt_block())
        if ctx.DOLLAR_ID():
            id = Id(ctx.DOLLAR_ID().getText())
        elif ctx.ID().getText() == 'main':
            class_type = ctx.parentCtx.parentCtx.parentCtx
            if param == [] and class_type.ID(0).getText() == 'Program':
                kind = Static()
            else:
                kind = Instance()
            id = Id('main')
        else:
            kind = Instance()
            id = Id(ctx.ID().getText())
        return [MethodDecl(kind, id, param, body)]

    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        name = Id("Constructor")
        param = []
        if ctx.list_param():
            param = self.visit(ctx.list_param())
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(kind, name, param, body)]

    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        name = Id("Destructor")
        param = []
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(kind, name, param, body)]

    # Visit a parse tree produced by D96Parser#attr_decl_1.
    def visitAttr_decl_1(self, ctx: D96Parser.Attr_decl_1Context):
        id_list = self.visit(ctx.idList())
        type_ = self.visit(ctx.typeDeclaration())
        return id_list, type_

    # Visit a parse tree produced by D96Parser#attr_decl_2.
    def visitAttr_decl_2(self, ctx: D96Parser.Attr_decl_2Context):
        id_type = self.visit(ctx.id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_1())
        lst1.append(id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#extend_1.
    def visitExtend_1(self, ctx: D96Parser.Extend_1Context):
        if ctx.typeDeclaration():
            return [], [], self.visit(ctx.typeDeclaration())
        id_type = self.visit(ctx.id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_1())
        lst1.append(id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#id_type.
    def visitId_type(self, ctx: D96Parser.Id_typeContext):
        return Id(ctx.getChild(0).getText())

    # Visit a parse tree produced by D96Parser#idList.
    def visitIdList(self, ctx: D96Parser.IdListContext):
        return [self.visit(i) for i in ctx.id_type()]

    # Visit a parse tree produced by D96Parser#nor_id_type.
    def visitNor_id_type(self, ctx: D96Parser.Nor_id_typeContext):
        return Id(ctx.ID().getText())

    # Visit a parse tree produced by D96Parser#nor_idList.
    def visitNor_idList(self, ctx: D96Parser.Nor_idListContext):
        return [self.visit(i) for i in ctx.nor_id_type()]

    # Visit a parse tree produced by D96Parser#vari_decl_1.
    def visitVari_decl_1(self, ctx: D96Parser.Vari_decl_1Context):
        nor_idList = self.visit(ctx.nor_idList())
        type_ = self.visit(ctx.typeDeclaration())
        return nor_idList, type_

    # Visit a parse tree produced by D96Parser#vari_decl_2.
    def visitVari_decl_2(self, ctx: D96Parser.Vari_decl_2Context):
        nor_id_type = self.visit(ctx.nor_id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_2())
        lst1.append(nor_id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#extend_2.
    def visitExtend_2(self, ctx: D96Parser.Extend_2Context):
        if ctx.typeDeclaration():
            return [], [], self.visit(ctx.typeDeclaration())
        nor_id_type = self.visit(ctx.nor_id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_2())
        lst1.append(nor_id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#typeDeclaration.
    def visitTypeDeclaration(self, ctx: D96Parser.TypeDeclarationContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.K_BOOLEAN():
            return BoolType()
        elif ctx.K_INT():
            return IntType()
        elif ctx.K_FLOAT():
            return FloatType()
        elif ctx.K_STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by D96Parser#typeDeclaration2.
    def visitTypeDeclaration2(self, ctx: D96Parser.TypeDeclaration2Context):
        if ctx.K_BOOLEAN():
            return BoolType()
        elif ctx.K_INT():
            return IntType()
        elif ctx.K_FLOAT():
            return FloatType()
        elif ctx.K_STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        eleType = self.visit(ctx.typeDeclaration2())
        size = text2int(ctx.INT2().getText())
        return ArrayType(size, eleType)

    # Visit a parse tree produced by D96Parser#list_param.
    def visitList_param(self, ctx: D96Parser.List_paramContext):
        return flatten([self.visit(i) for i in ctx.param_decl()])

    # Visit a parse tree produced by D96Parser#param_decl.
    def visitParam_decl(self, ctx: D96Parser.Param_declContext):
        id_list = self.visit(ctx.nor_idList())
        type_decl = self.visit(ctx.typeDeclaration())
        var_decl_list = []
        for i in id_list:
            var_decl_list += [VarDecl(i, type_decl)]
        return var_decl_list  # Return [VarDecl(1, Int), VarDecl(2, Int)]

    # Visit a parse tree produced by D96Parser#stmt_block.
    def visitStmt_block(self, ctx: D96Parser.Stmt_blockContext):
        return Block(flatten([self.visit(i) for i in ctx.stmt()]))

    # Visit a parse tree produced by D96Parser#stmt_block_ret.
    def visitStmt_block_ret(self, ctx: D96Parser.Stmt_block_retContext):
        return [Block(flatten([self.visit(i) for i in ctx.stmt()]))]

    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#vari_decl.
    def visitVari_decl(self, ctx: D96Parser.Vari_declContext):
        if ctx.VAL():
            if ctx.vari_decl_1():
                nor_id_list, type_ = self.visit(ctx.vari_decl_1())
                # if "Id(" in str(type_):
                #     return [ConstDecl(i, type_, NullLiteral()) for i in nor_id_list]
                return [ConstDecl(i, type_) for i in nor_id_list]
            lst1, lst2, type_ = self.visit(ctx.vari_decl_2())
            length = len(lst1)
            lst1.reverse()
            # ret = [(Id("a"), 2), IntType]
            return [ConstDecl(lst1[i], type_, lst2[i]) for i in range(length)]
        # If ctx.VAR()
        if ctx.vari_decl_1():
            nor_id_list, type_ = self.visit(ctx.vari_decl_1())
            if "Id(" in str(type_):
                return [VarDecl(i, type_, NullLiteral()) for i in nor_id_list]
            return [VarDecl(i, type_) for i in nor_id_list]
        lst1, lst2, type_ = self.visit(ctx.vari_decl_2())
        length = len(lst1)
        lst1.reverse()
        return [VarDecl(lst1[i], type_, lst2[i]) for i in range(length)]

    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        if ctx.expr8():
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.index_op())
            lhs = ArrayCell(arr, idx)
        elif ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visit(ctx.member_access_attribute())
        rhs = self.visit(ctx.expr())
        return [Assign(lhs, rhs)]

    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr, block = self.visit(ctx.condition_block())
        else_block = self.visit(ctx.elseif_blocks())
        return [If(expr, block, else_block)]

    # Visit a parse tree produced by D96Parser#condition_block.
    def visitCondition_block(self, ctx: D96Parser.Condition_blockContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.stmt_block())
        return expr, block

    # Visit a parse tree produced by D96Parser#elseif_block.
    def visitElseif_block(self, ctx: D96Parser.Elseif_blockContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.stmt_block())
        return expr, block

    # Visit a parse tree produced by D96Parser#elseif_blocks.
    def visitElseif_blocks(self, ctx: D96Parser.Elseif_blocksContext):
        if ctx.else_block():
            return self.visit(ctx.else_block())
        if ctx.elseif_block():
            expr, block = self.visit(ctx.elseif_block())
            else_block = self.visit(ctx.elseif_blocks())
            return If(expr, block, else_block)
        return None

    # Visit a parse tree produced by D96Parser#else_block.
    def visitElse_block(self, ctx: D96Parser.Else_blockContext):
        return self.visit(ctx.stmt_block())

    # Visit a parse tree produced by D96Parser#for_each_stmt.
    def visitFor_each_stmt(self, ctx: D96Parser.For_each_stmtContext):
        id = Id(ctx.ID().getText())  # TODO: Convert to ID Id('á()')
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        loop = self.visit(ctx.stmt_block())
        expr3 = IntLiteral(1)
        if ctx.expr(2):
            expr3 = self.visit(ctx.expr(2))
        return [For(id, expr1, expr2, loop, expr3)]

    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return [Break()]

    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return [Continue()]

    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return [Return(expr)]

    # Visit a parse tree produced by D96Parser#method_inv_stmt.
    def visitMethod_inv_stmt(self, ctx: D96Parser.Method_inv_stmtContext):
        obj, method, param = self.visit(ctx.member_access_method())
        return [CallStmt(obj, method, param)]

    # Visit a parse tree produced by D96Parser#new_stmt.
    def visitNew_stmt(self, ctx: D96Parser.New_stmtContext):
        id = Id(ctx.ID().getText())
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        return [NewExpr(id, list_expr)]

    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.expr1(1):
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            op = '==.'
            if ctx.ADD_STRING():
                op = '+.'
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr1(0))

    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.expr2(1):
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            op = '=='
            if ctx.NOT_EQ_COMPARE():
                op = '!='
            elif ctx.SMALLER():
                op = '<'
            elif ctx.GREATER():
                op = '>'
            elif ctx.GR_OR_EQ():
                op = '>='
            elif ctx.SM_OR_EQ():
                op = '<='
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr2(0))

    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.expr2():
            op = '&&'
            if ctx.OR_():
                op = '||'
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.expr3():
            op = '+'
            if ctx.MINUS_():
                op = '-'
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.expr4():
            op = '*'
            if ctx.DIV_():
                op = '/'
            elif ctx.MOD_():
                op = '%'
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr5())

    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        body = self.visit(ctx.expr5())
        return UnaryOp('!', body)

    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        body = self.visit(ctx.expr6())
        return UnaryOp('-', body)

    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.index_op():
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.index_op())
            return ArrayCell(arr, idx)
        return self.visit(ctx.expr8())

    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.expr9():
            return self.visit(ctx.expr9())
        first = self.visit(ctx.expr8())
        second = Id(ctx.ID().getText())
        if ctx.LB():  # If it is a Static method
            list_expr = []
            if ctx.list_expr():
                list_expr = self.visit(ctx.list_expr())
            return CallExpr(first, second, list_expr)
        # If it is normal attribute access
        return FieldAccess(first, second)

    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.expr10():
            return self.visit(ctx.expr10())
        first = Id(ctx.ID().getText())
        second = Id(ctx.DOLLAR_ID().getText())
        if ctx.LB():  # If it is a Static method
            list_expr = []
            if ctx.list_expr():
                list_expr = self.visit(ctx.list_expr())
            return CallExpr(first, second, list_expr)
        # If it is normal attribute access
        return FieldAccess(first, second)

    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.primary():
            return self.visit(ctx.primary())
        id = Id(ctx.ID().getText())
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        return NewExpr(id, list_expr)

    # Visit a parse tree produced by D96Parser#primary.
    def visitPrimary(self, ctx: D96Parser.PrimaryContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.INT2():
            return IntLiteral(text2int(ctx.INT2().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.literal())
        # Return literal

    # Visit a parse tree produced by D96Parser#list_expr.
    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        return [self.visit(i) for i in ctx.expr()]
        # Return [Expr(), Expr(), ]

    # Visit a parse tree produced by D96Parser#index_op.
    def visitIndex_op(self, ctx: D96Parser.Index_opContext):
        return [self.visit(i) for i in ctx.expr()]
        # Return [Expr(), Expr(), ]

    # Visit a parse tree produced by D96Parser#member_access_attribute.
    def visitMember_access_attribute(self, ctx: D96Parser.Member_access_attributeContext):
        id = Id(ctx.ID().getText())
        if ctx.expr8():
            expr8 = self.visit(ctx.expr8())
            return FieldAccess(expr8, id)
        dollar_id = Id(ctx.DOLLAR_ID().getText())
        return FieldAccess(id, dollar_id)
        # Return a.a or a::$a

    # Visit a parse tree produced by D96Parser#member_access_method.
    def visitMember_access_method(self, ctx: D96Parser.Member_access_methodContext):
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        id = Id(ctx.ID().getText())
        if ctx.expr8():
            expr8 = self.visit(ctx.expr8())
            return expr8, id, list_expr
        dollar_id = Id(ctx.DOLLAR_ID().getText())
        return id, dollar_id, list_expr

        # Visit a parse tree produced by D96Parser#literal.

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INT():
            return IntLiteral(text2int(ctx.INT().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText() == 'True')
        elif ctx.FLOAT():
            return FloatLiteral(text2float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        return self.visit(ctx.iarray())
        # Return Literal or expression

    # Visit a parse tree produced by D96Parser#farray.
    def visitFarray(self, ctx: D96Parser.FarrayContext):
        return self.visit(ctx.getChild(0))
        # Visit int_array, float_array ...

    def visitInt_int2(self, ctx: D96Parser.Int_int2Context):
        return IntLiteral(text2int(ctx.getChild(0).getText()))

    # Visit a parse tree produced by D96Parser#int_array.
    def visitInt_array(self, ctx: D96Parser.Int_arrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.int_int2()])

    # Visit a parse tree produced by D96Parser#float_array.
    def visitFloat_array(self, ctx: D96Parser.Float_arrayContext):
        return ArrayLiteral([FloatLiteral(text2float(i.getText())) for i in ctx.FLOAT()])

    # Visit a parse tree produced by D96Parser#string_array.
    def visitString_array(self, ctx: D96Parser.String_arrayContext):
        return ArrayLiteral([StringLiteral(i.getText()) for i in ctx.STRING()])

    # Visit a parse tree produced by D96Parser#boolean_array.
    def visitBoolean_array(self, ctx: D96Parser.Boolean_arrayContext):
        return ArrayLiteral([BooleanLiteral(i.getText() == 'True') for i in ctx.BOOLEAN()])

    # Visit a parse tree produced by D96Parser#iarray.
    def visitIarray(self, ctx: D96Parser.IarrayContext):
        return self.visit(ctx.getChild(0))  # Visit the child iarray, farray

    # Visit a parse tree produced by D96Parser#marray.
    def visitMarray(self, ctx: D96Parser.MarrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.iarray()])  # Return [iarray, iarray,...]

    def visitExpr_array(self, ctx: D96Parser.Expr_arrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.expr()])


# from D96Visitor import D96Visitor
i = 0
if i == 1:
    from initial.target.D96Visitor import D96Visitor
    from initial.target.D96Parser import D96Parser
    from initial.src.main.d96.utils.AST import *

from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

from functools import reduce


def flatten(lst):
    return reduce(lambda x, y: x + y, lst, [])


def text2float(text):
    if text[0] == '.' and (text[1] == 'e' or text[1] == 'E'):
        return float('0' + text)
    return float(text)


def text2int(text):
    if text[0] != '0':
        return int(text)
    elif text == '0':
        return 0
    elif text[1] in ['x', 'X']:
        return int(text, 16)
    elif text[1] in ['b', 'B']:
        return int(text, 2)
    return int(text[0] + 'o' + text[1:], 8)


class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        a = [self.visit(i) for i in ctx.class_decl()]
        # a = flatten(a)
        return Program(a)

    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        return self.visit(ctx.class_type())

    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.class_block())
        memlist = flatten(memlist)
        parentname: Id = None
        if ctx.ID(1):
            parentname = Id(ctx.ID(1).getText())
        # TODO: Check static main instance
        return ClassDecl(classname, memlist, parentname)

    # Visit a parse tree produced by D96Parser#class_block.
    def visitClass_block(self, ctx: D96Parser.Class_blockContext):
        return [self.visit(i) for i in ctx.class_stmt()]

    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx: D96Parser.Class_stmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        if ctx.VAL():  # TODO: Check declare null classtype
            if ctx.attr_decl_1():
                idList, type_ = self.visit(ctx.attr_decl_1())
                # if "Id(" in str(type_):
                #     return [
                #         AttributeDecl(Static(), ConstDecl(i, type_, NullLiteral())) if '$' in str(i) else AttributeDecl(
                #             Instance(), ConstDecl(i, type_, NullLiteral())) for i in idList]
                return [AttributeDecl(Static(), ConstDecl(i, type_)) if '$' in str(i) else AttributeDecl(Instance(),
                                                                                                         ConstDecl(i,
                                                                                                                   type_))
                        for i in idList]
            lst1, lst2, type_ = self.visit(ctx.attr_decl_2())
            length = len(lst1)
            lst1.reverse()
            # ret = [(Id("a"), 2), IntType]
            return [
                AttributeDecl(Static(), ConstDecl(lst1[i], type_, lst2[i])) if '$' in str(lst1[i]) else AttributeDecl(
                    Instance(), ConstDecl(lst1[i], type_, lst2[i])) for i in range(length)]

        # Variable
        if ctx.attr_decl_1():
            idList, type_ = self.visit(ctx.attr_decl_1())
            if "Id(" in str(type_):
                return [AttributeDecl(Static(), VarDecl(i, type_, NullLiteral())) if '$' in str(i) else AttributeDecl(
                    Instance(), VarDecl(i, type_, NullLiteral())) for i in idList]
            return [AttributeDecl(Static(), VarDecl(i, type_)) if '$' in str(i) else AttributeDecl(Instance(),
                                                                                                   VarDecl(i, type_))
                    for i in idList]
        lst1, lst2, type_ = self.visit(ctx.attr_decl_2())
        length = len(lst1)
        lst1.reverse()
        # ret = [(Id("a"), 2), IntType]
        return [AttributeDecl(Static(), VarDecl(lst1[i], type_, lst2[i])) if '$' in str(lst1[i]) else AttributeDecl(
            Instance(), VarDecl(lst1[i], type_, lst2[i])) for i in range(length)]

    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        kind = Static()
        param = []
        if ctx.list_param():
            param = self.visit(ctx.list_param())
        body = self.visit(ctx.stmt_block())
        if ctx.DOLLAR_ID():
            id = Id(ctx.DOLLAR_ID().getText())
        elif ctx.ID().getText() == 'main':
            class_type = ctx.parentCtx.parentCtx.parentCtx
            if param == [] and class_type.ID(0).getText() == 'Program':
                kind = Static()
            else:
                kind = Instance()
            id = Id('main')
        else:
            kind = Instance()
            id = Id(ctx.ID().getText())
        return [MethodDecl(kind, id, param, body)]

    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        name = Id("Constructor")
        param = []
        if ctx.list_param():
            param = self.visit(ctx.list_param())
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(kind, name, param, body)]

    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        name = Id("Destructor")
        param = []
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(kind, name, param, body)]

    # Visit a parse tree produced by D96Parser#attr_decl_1.
    def visitAttr_decl_1(self, ctx: D96Parser.Attr_decl_1Context):
        id_list = self.visit(ctx.idList())
        type_ = self.visit(ctx.typeDeclaration())
        return id_list, type_

    # Visit a parse tree produced by D96Parser#attr_decl_2.
    def visitAttr_decl_2(self, ctx: D96Parser.Attr_decl_2Context):
        id_type = self.visit(ctx.id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_1())
        lst1.append(id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#extend_1.
    def visitExtend_1(self, ctx: D96Parser.Extend_1Context):
        if ctx.typeDeclaration():
            return [], [], self.visit(ctx.typeDeclaration())
        id_type = self.visit(ctx.id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_1())
        lst1.append(id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#id_type.
    def visitId_type(self, ctx: D96Parser.Id_typeContext):
        return Id(ctx.getChild(0).getText())

    # Visit a parse tree produced by D96Parser#idList.
    def visitIdList(self, ctx: D96Parser.IdListContext):
        return [self.visit(i) for i in ctx.id_type()]

    # Visit a parse tree produced by D96Parser#nor_id_type.
    def visitNor_id_type(self, ctx: D96Parser.Nor_id_typeContext):
        return Id(ctx.ID().getText())

    # Visit a parse tree produced by D96Parser#nor_idList.
    def visitNor_idList(self, ctx: D96Parser.Nor_idListContext):
        return [self.visit(i) for i in ctx.nor_id_type()]

    # Visit a parse tree produced by D96Parser#vari_decl_1.
    def visitVari_decl_1(self, ctx: D96Parser.Vari_decl_1Context):
        nor_idList = self.visit(ctx.nor_idList())
        type_ = self.visit(ctx.typeDeclaration())
        return nor_idList, type_

    # Visit a parse tree produced by D96Parser#vari_decl_2.
    def visitVari_decl_2(self, ctx: D96Parser.Vari_decl_2Context):
        nor_id_type = self.visit(ctx.nor_id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_2())
        lst1.append(nor_id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#extend_2.
    def visitExtend_2(self, ctx: D96Parser.Extend_2Context):
        if ctx.typeDeclaration():
            return [], [], self.visit(ctx.typeDeclaration())
        nor_id_type = self.visit(ctx.nor_id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_2())
        lst1.append(nor_id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#typeDeclaration.
    def visitTypeDeclaration(self, ctx: D96Parser.TypeDeclarationContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.K_BOOLEAN():
            return BoolType()
        elif ctx.K_INT():
            return IntType()
        elif ctx.K_FLOAT():
            return FloatType()
        elif ctx.K_STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by D96Parser#typeDeclaration2.
    def visitTypeDeclaration2(self, ctx: D96Parser.TypeDeclaration2Context):
        if ctx.K_BOOLEAN():
            return BoolType()
        elif ctx.K_INT():
            return IntType()
        elif ctx.K_FLOAT():
            return FloatType()
        elif ctx.K_STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        eleType = self.visit(ctx.typeDeclaration2())
        size = text2int(ctx.INT2().getText())
        return ArrayType(size, eleType)

    # Visit a parse tree produced by D96Parser#list_param.
    def visitList_param(self, ctx: D96Parser.List_paramContext):
        return flatten([self.visit(i) for i in ctx.param_decl()])

    # Visit a parse tree produced by D96Parser#param_decl.
    def visitParam_decl(self, ctx: D96Parser.Param_declContext):
        id_list = self.visit(ctx.nor_idList())
        type_decl = self.visit(ctx.typeDeclaration())
        var_decl_list = []
        for i in id_list:
            var_decl_list += [VarDecl(i, type_decl)]
        return var_decl_list  # Return [VarDecl(1, Int), VarDecl(2, Int)]

    # Visit a parse tree produced by D96Parser#stmt_block.
    def visitStmt_block(self, ctx: D96Parser.Stmt_blockContext):
        return Block(flatten([self.visit(i) for i in ctx.stmt()]))

    # Visit a parse tree produced by D96Parser#stmt_block_ret.
    def visitStmt_block_ret(self, ctx: D96Parser.Stmt_block_retContext):
        return [Block(flatten([self.visit(i) for i in ctx.stmt()]))]

    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#vari_decl.
    def visitVari_decl(self, ctx: D96Parser.Vari_declContext):
        if ctx.VAL():
            if ctx.vari_decl_1():
                nor_id_list, type_ = self.visit(ctx.vari_decl_1())
                # if "Id(" in str(type_):
                #     return [ConstDecl(i, type_, NullLiteral()) for i in nor_id_list]
                return [ConstDecl(i, type_) for i in nor_id_list]
            lst1, lst2, type_ = self.visit(ctx.vari_decl_2())
            length = len(lst1)
            lst1.reverse()
            # ret = [(Id("a"), 2), IntType]
            return [ConstDecl(lst1[i], type_, lst2[i]) for i in range(length)]
        # If ctx.VAR()
        if ctx.vari_decl_1():
            nor_id_list, type_ = self.visit(ctx.vari_decl_1())
            if "Id(" in str(type_):
                return [VarDecl(i, type_, NullLiteral()) for i in nor_id_list]
            return [VarDecl(i, type_) for i in nor_id_list]
        lst1, lst2, type_ = self.visit(ctx.vari_decl_2())
        length = len(lst1)
        lst1.reverse()
        return [VarDecl(lst1[i], type_, lst2[i]) for i in range(length)]

    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        if ctx.expr8():
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.index_op())
            lhs = ArrayCell(arr, idx)
        elif ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visit(ctx.member_access_attribute())
        rhs = self.visit(ctx.expr())
        return [Assign(lhs, rhs)]

    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr, block = self.visit(ctx.condition_block())
        else_block = self.visit(ctx.elseif_blocks())
        return [If(expr, block, else_block)]

    # Visit a parse tree produced by D96Parser#condition_block.
    def visitCondition_block(self, ctx: D96Parser.Condition_blockContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.stmt_block())
        return expr, block

    # Visit a parse tree produced by D96Parser#elseif_block.
    def visitElseif_block(self, ctx: D96Parser.Elseif_blockContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.stmt_block())
        return expr, block

    # Visit a parse tree produced by D96Parser#elseif_blocks.
    def visitElseif_blocks(self, ctx: D96Parser.Elseif_blocksContext):
        if ctx.else_block():
            return self.visit(ctx.else_block())
        if ctx.elseif_block():
            expr, block = self.visit(ctx.elseif_block())
            else_block = self.visit(ctx.elseif_blocks())
            return If(expr, block, else_block)
        return None

    # Visit a parse tree produced by D96Parser#else_block.
    def visitElse_block(self, ctx: D96Parser.Else_blockContext):
        return self.visit(ctx.stmt_block())

    # Visit a parse tree produced by D96Parser#for_each_stmt.
    def visitFor_each_stmt(self, ctx: D96Parser.For_each_stmtContext):
        id = Id(ctx.ID().getText())  # TODO: Convert to ID Id('á()')
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        loop = self.visit(ctx.stmt_block())
        expr3 = IntLiteral(1)
        if ctx.expr(2):
            expr3 = self.visit(ctx.expr(2))
        return [For(id, expr1, expr2, loop, expr3)]

    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return [Break()]

    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return [Continue()]

    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return [Return(expr)]

    # Visit a parse tree produced by D96Parser#method_inv_stmt.
    def visitMethod_inv_stmt(self, ctx: D96Parser.Method_inv_stmtContext):
        obj, method, param = self.visit(ctx.member_access_method())
        return [CallStmt(obj, method, param)]

    # Visit a parse tree produced by D96Parser#new_stmt.
    def visitNew_stmt(self, ctx: D96Parser.New_stmtContext):
        id = Id(ctx.ID().getText())
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        return [NewExpr(id, list_expr)]

    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.expr1(1):
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            op = '==.'
            if ctx.ADD_STRING():
                op = '+.'
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr1(0))

    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.expr2(1):
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            op = '=='
            if ctx.NOT_EQ_COMPARE():
                op = '!='
            elif ctx.SMALLER():
                op = '<'
            elif ctx.GREATER():
                op = '>'
            elif ctx.GR_OR_EQ():
                op = '>='
            elif ctx.SM_OR_EQ():
                op = '<='
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr2(0))

    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.expr2():
            op = '&&'
            if ctx.OR_():
                op = '||'
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.expr3():
            op = '+'
            if ctx.MINUS_():
                op = '-'
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.expr4():
            op = '*'
            if ctx.DIV_():
                op = '/'
            elif ctx.MOD_():
                op = '%'
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr5())

    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        body = self.visit(ctx.expr5())
        return UnaryOp('!', body)

    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        body = self.visit(ctx.expr6())
        return UnaryOp('-', body)

    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.index_op():
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.index_op())
            return ArrayCell(arr, idx)
        return self.visit(ctx.expr8())

    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.expr9():
            return self.visit(ctx.expr9())
        first = self.visit(ctx.expr8())
        second = Id(ctx.ID().getText())
        if ctx.LB():  # If it is a Static method
            list_expr = []
            if ctx.list_expr():
                list_expr = self.visit(ctx.list_expr())
            return CallExpr(first, second, list_expr)
        # If it is normal attribute access
        return FieldAccess(first, second)

    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.expr10():
            return self.visit(ctx.expr10())
        first = Id(ctx.ID().getText())
        second = Id(ctx.DOLLAR_ID().getText())
        if ctx.LB():  # If it is a Static method
            list_expr = []
            if ctx.list_expr():
                list_expr = self.visit(ctx.list_expr())
            return CallExpr(first, second, list_expr)
        # If it is normal attribute access
        return FieldAccess(first, second)

    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.primary():
            return self.visit(ctx.primary())
        id = Id(ctx.ID().getText())
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        return NewExpr(id, list_expr)

    # Visit a parse tree produced by D96Parser#primary.
    def visitPrimary(self, ctx: D96Parser.PrimaryContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.INT2():
            return IntLiteral(text2int(ctx.INT2().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.literal())
        # Return literal

    # Visit a parse tree produced by D96Parser#list_expr.
    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        return [self.visit(i) for i in ctx.expr()]
        # Return [Expr(), Expr(), ]

    # Visit a parse tree produced by D96Parser#index_op.
    def visitIndex_op(self, ctx: D96Parser.Index_opContext):
        return [self.visit(i) for i in ctx.expr()]
        # Return [Expr(), Expr(), ]

    # Visit a parse tree produced by D96Parser#member_access_attribute.
    def visitMember_access_attribute(self, ctx: D96Parser.Member_access_attributeContext):
        id = Id(ctx.ID().getText())
        if ctx.expr8():
            expr8 = self.visit(ctx.expr8())
            return FieldAccess(expr8, id)
        dollar_id = Id(ctx.DOLLAR_ID().getText())
        return FieldAccess(id, dollar_id)
        # Return a.a or a::$a

    # Visit a parse tree produced by D96Parser#member_access_method.
    def visitMember_access_method(self, ctx: D96Parser.Member_access_methodContext):
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        id = Id(ctx.ID().getText())
        if ctx.expr8():
            expr8 = self.visit(ctx.expr8())
            return expr8, id, list_expr
        dollar_id = Id(ctx.DOLLAR_ID().getText())
        return id, dollar_id, list_expr

        # Visit a parse tree produced by D96Parser#literal.

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INT():
            return IntLiteral(text2int(ctx.INT().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText() == 'True')
        elif ctx.FLOAT():
            return FloatLiteral(text2float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        return self.visit(ctx.iarray())
        # Return Literal or expression

    # Visit a parse tree produced by D96Parser#farray.
    def visitFarray(self, ctx: D96Parser.FarrayContext):
        return self.visit(ctx.getChild(0))
        # Visit int_array, float_array ...

    def visitInt_int2(self, ctx: D96Parser.Int_int2Context):
        return IntLiteral(text2int(ctx.getChild(0).getText()))

    # Visit a parse tree produced by D96Parser#int_array.
    def visitInt_array(self, ctx: D96Parser.Int_arrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.int_int2()])

    # Visit a parse tree produced by D96Parser#float_array.
    def visitFloat_array(self, ctx: D96Parser.Float_arrayContext):
        return ArrayLiteral([FloatLiteral(text2float(i.getText())) for i in ctx.FLOAT()])

    # Visit a parse tree produced by D96Parser#string_array.
    def visitString_array(self, ctx: D96Parser.String_arrayContext):
        return ArrayLiteral([StringLiteral(i.getText()) for i in ctx.STRING()])

    # Visit a parse tree produced by D96Parser#boolean_array.
    def visitBoolean_array(self, ctx: D96Parser.Boolean_arrayContext):
        return ArrayLiteral([BooleanLiteral(i.getText() == 'True') for i in ctx.BOOLEAN()])

    # Visit a parse tree produced by D96Parser#iarray.
    def visitIarray(self, ctx: D96Parser.IarrayContext):
        return self.visit(ctx.getChild(0))  # Visit the child iarray, farray

    # Visit a parse tree produced by D96Parser#marray.
    def visitMarray(self, ctx: D96Parser.MarrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.iarray()])  # Return [iarray, iarray,...]

    def visitExpr_array(self, ctx: D96Parser.Expr_arrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.expr()])


# from D96Visitor import D96Visitor
i = 0
if i == 1:
    from initial.target.D96Visitor import D96Visitor
    from initial.target.D96Parser import D96Parser
    from initial.src.main.d96.utils.AST import *

from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

from functools import reduce


def flatten(lst):
    return reduce(lambda x, y: x + y, lst, [])


def text2float(text):
    if text[0] == '.' and (text[1] == 'e' or text[1] == 'E'):
        return float('0' + text)
    return float(text)


def text2int(text):
    if text[0] != '0':
        return int(text)
    elif text == '0':
        return 0
    elif text[1] in ['x', 'X']:
        return int(text, 16)
    elif text[1] in ['b', 'B']:
        return int(text, 2)
    return int(text[0] + 'o' + text[1:], 8)


class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        a = [self.visit(i) for i in ctx.class_decl()]
        # a = flatten(a)
        return Program(a)

    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        return self.visit(ctx.class_type())

    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.class_block())
        memlist = flatten(memlist)
        parentname: Id = None
        if ctx.ID(1):
            parentname = Id(ctx.ID(1).getText())
        # TODO: Check static main instance
        return ClassDecl(classname, memlist, parentname)

    # Visit a parse tree produced by D96Parser#class_block.
    def visitClass_block(self, ctx: D96Parser.Class_blockContext):
        return [self.visit(i) for i in ctx.class_stmt()]

    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx: D96Parser.Class_stmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        if ctx.VAL():  # TODO: Check declare null classtype
            if ctx.attr_decl_1():
                idList, type_ = self.visit(ctx.attr_decl_1())
                # if "Id(" in str(type_):
                #     return [
                #         AttributeDecl(Static(), ConstDecl(i, type_, NullLiteral())) if '$' in str(i) else AttributeDecl(
                #             Instance(), ConstDecl(i, type_, NullLiteral())) for i in idList]
                return [AttributeDecl(Static(), ConstDecl(i, type_)) if '$' in str(i) else AttributeDecl(Instance(),
                                                                                                         ConstDecl(i,
                                                                                                                   type_))
                        for i in idList]
            lst1, lst2, type_ = self.visit(ctx.attr_decl_2())
            length = len(lst1)
            lst1.reverse()
            # ret = [(Id("a"), 2), IntType]
            return [
                AttributeDecl(Static(), ConstDecl(lst1[i], type_, lst2[i])) if '$' in str(lst1[i]) else AttributeDecl(
                    Instance(), ConstDecl(lst1[i], type_, lst2[i])) for i in range(length)]

        # Variable
        if ctx.attr_decl_1():
            idList, type_ = self.visit(ctx.attr_decl_1())
            if "Id(" in str(type_):
                return [AttributeDecl(Static(), VarDecl(i, type_, NullLiteral())) if '$' in str(i) else AttributeDecl(
                    Instance(), VarDecl(i, type_, NullLiteral())) for i in idList]
            return [AttributeDecl(Static(), VarDecl(i, type_)) if '$' in str(i) else AttributeDecl(Instance(),
                                                                                                   VarDecl(i, type_))
                    for i in idList]
        lst1, lst2, type_ = self.visit(ctx.attr_decl_2())
        length = len(lst1)
        lst1.reverse()
        # ret = [(Id("a"), 2), IntType]
        return [AttributeDecl(Static(), VarDecl(lst1[i], type_, lst2[i])) if '$' in str(lst1[i]) else AttributeDecl(
            Instance(), VarDecl(lst1[i], type_, lst2[i])) for i in range(length)]

    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        kind = Static()
        param = []
        if ctx.list_param():
            param = self.visit(ctx.list_param())
        body = self.visit(ctx.stmt_block())
        if ctx.DOLLAR_ID():
            id = Id(ctx.DOLLAR_ID().getText())
        elif ctx.ID().getText() == 'main':
            class_type = ctx.parentCtx.parentCtx.parentCtx
            if param == [] and class_type.ID(0).getText() == 'Program':
                kind = Static()
            else:
                kind = Instance()
            id = Id('main')
        else:
            kind = Instance()
            id = Id(ctx.ID().getText())
        return [MethodDecl(kind, id, param, body)]

    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        name = Id("Constructor")
        param = []
        if ctx.list_param():
            param = self.visit(ctx.list_param())
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(kind, name, param, body)]

    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        name = Id("Destructor")
        param = []
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(kind, name, param, body)]

    # Visit a parse tree produced by D96Parser#attr_decl_1.
    def visitAttr_decl_1(self, ctx: D96Parser.Attr_decl_1Context):
        id_list = self.visit(ctx.idList())
        type_ = self.visit(ctx.typeDeclaration())
        return id_list, type_

    # Visit a parse tree produced by D96Parser#attr_decl_2.
    def visitAttr_decl_2(self, ctx: D96Parser.Attr_decl_2Context):
        id_type = self.visit(ctx.id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_1())
        lst1.append(id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#extend_1.
    def visitExtend_1(self, ctx: D96Parser.Extend_1Context):
        if ctx.typeDeclaration():
            return [], [], self.visit(ctx.typeDeclaration())
        id_type = self.visit(ctx.id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_1())
        lst1.append(id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#id_type.
    def visitId_type(self, ctx: D96Parser.Id_typeContext):
        return Id(ctx.getChild(0).getText())

    # Visit a parse tree produced by D96Parser#idList.
    def visitIdList(self, ctx: D96Parser.IdListContext):
        return [self.visit(i) for i in ctx.id_type()]

    # Visit a parse tree produced by D96Parser#nor_id_type.
    def visitNor_id_type(self, ctx: D96Parser.Nor_id_typeContext):
        return Id(ctx.ID().getText())

    # Visit a parse tree produced by D96Parser#nor_idList.
    def visitNor_idList(self, ctx: D96Parser.Nor_idListContext):
        return [self.visit(i) for i in ctx.nor_id_type()]

    # Visit a parse tree produced by D96Parser#vari_decl_1.
    def visitVari_decl_1(self, ctx: D96Parser.Vari_decl_1Context):
        nor_idList = self.visit(ctx.nor_idList())
        type_ = self.visit(ctx.typeDeclaration())
        return nor_idList, type_

    # Visit a parse tree produced by D96Parser#vari_decl_2.
    def visitVari_decl_2(self, ctx: D96Parser.Vari_decl_2Context):
        nor_id_type = self.visit(ctx.nor_id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_2())
        lst1.append(nor_id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#extend_2.
    def visitExtend_2(self, ctx: D96Parser.Extend_2Context):
        if ctx.typeDeclaration():
            return [], [], self.visit(ctx.typeDeclaration())
        nor_id_type = self.visit(ctx.nor_id_type())
        expr = self.visit(ctx.expr())
        lst1, lst2, type_ = self.visit(ctx.extend_2())
        lst1.append(nor_id_type)
        lst2.append(expr)
        return lst1, lst2, type_

    # Visit a parse tree produced by D96Parser#typeDeclaration.
    def visitTypeDeclaration(self, ctx: D96Parser.TypeDeclarationContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.K_BOOLEAN():
            return BoolType()
        elif ctx.K_INT():
            return IntType()
        elif ctx.K_FLOAT():
            return FloatType()
        elif ctx.K_STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by D96Parser#typeDeclaration2.
    def visitTypeDeclaration2(self, ctx: D96Parser.TypeDeclaration2Context):
        if ctx.K_BOOLEAN():
            return BoolType()
        elif ctx.K_INT():
            return IntType()
        elif ctx.K_FLOAT():
            return FloatType()
        elif ctx.K_STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        eleType = self.visit(ctx.typeDeclaration2())
        size = text2int(ctx.INT2().getText())
        return ArrayType(size, eleType)

    # Visit a parse tree produced by D96Parser#list_param.
    def visitList_param(self, ctx: D96Parser.List_paramContext):
        return flatten([self.visit(i) for i in ctx.param_decl()])

    # Visit a parse tree produced by D96Parser#param_decl.
    def visitParam_decl(self, ctx: D96Parser.Param_declContext):
        id_list = self.visit(ctx.nor_idList())
        type_decl = self.visit(ctx.typeDeclaration())
        var_decl_list = []
        for i in id_list:
            var_decl_list += [VarDecl(i, type_decl)]
        return var_decl_list  # Return [VarDecl(1, Int), VarDecl(2, Int)]

    # Visit a parse tree produced by D96Parser#stmt_block.
    def visitStmt_block(self, ctx: D96Parser.Stmt_blockContext):
        return Block(flatten([self.visit(i) for i in ctx.stmt()]))

    # Visit a parse tree produced by D96Parser#stmt_block_ret.
    def visitStmt_block_ret(self, ctx: D96Parser.Stmt_block_retContext):
        return [Block(flatten([self.visit(i) for i in ctx.stmt()]))]

    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#vari_decl.
    def visitVari_decl(self, ctx: D96Parser.Vari_declContext):
        if ctx.VAL():
            if ctx.vari_decl_1():
                nor_id_list, type_ = self.visit(ctx.vari_decl_1())
                return [ConstDecl(i, type_) for i in nor_id_list]
            lst1, lst2, type_ = self.visit(ctx.vari_decl_2())
            length = len(lst1)
            lst1.reverse()
            # ret = [(Id("a"), 2), IntType]
            return [ConstDecl(lst1[i], type_, lst2[i]) for i in range(length)]
        # If ctx.VAR()
        if ctx.vari_decl_1():
            nor_id_list, type_ = self.visit(ctx.vari_decl_1())
            if "Id(" in str(type_):
                return [VarDecl(i, type_, NullLiteral()) for i in nor_id_list]
            return [VarDecl(i, type_) for i in nor_id_list]
        lst1, lst2, type_ = self.visit(ctx.vari_decl_2())
        length = len(lst1)
        lst1.reverse()
        return [VarDecl(lst1[i], type_, lst2[i]) for i in range(length)]

    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        if ctx.expr8():
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.index_op())
            lhs = ArrayCell(arr, idx)
        elif ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visit(ctx.member_access_attribute())
        rhs = self.visit(ctx.expr())
        return [Assign(lhs, rhs)]

    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr, block = self.visit(ctx.condition_block())
        else_block = self.visit(ctx.elseif_blocks())
        return [If(expr, block, else_block)]

    # Visit a parse tree produced by D96Parser#condition_block.
    def visitCondition_block(self, ctx: D96Parser.Condition_blockContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.stmt_block())
        return expr, block

    # Visit a parse tree produced by D96Parser#elseif_block.
    def visitElseif_block(self, ctx: D96Parser.Elseif_blockContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.stmt_block())
        return expr, block

    # Visit a parse tree produced by D96Parser#elseif_blocks.
    def visitElseif_blocks(self, ctx: D96Parser.Elseif_blocksContext):
        if ctx.else_block():
            return self.visit(ctx.else_block())
        if ctx.elseif_block():
            expr, block = self.visit(ctx.elseif_block())
            else_block = self.visit(ctx.elseif_blocks())
            return If(expr, block, else_block)
        return None

    # Visit a parse tree produced by D96Parser#else_block.
    def visitElse_block(self, ctx: D96Parser.Else_blockContext):
        return self.visit(ctx.stmt_block())

    # Visit a parse tree produced by D96Parser#for_each_stmt.
    def visitFor_each_stmt(self, ctx: D96Parser.For_each_stmtContext):
        id = Id(ctx.ID().getText())  # TODO: Convert to ID Id('á()')
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        loop = self.visit(ctx.stmt_block())
        expr3 = IntLiteral(1)
        if ctx.expr(2):
            expr3 = self.visit(ctx.expr(2))
        return [For(id, expr1, expr2, loop, expr3)]

    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return [Break()]

    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return [Continue()]

    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return [Return(expr)]

    # Visit a parse tree produced by D96Parser#method_inv_stmt.
    def visitMethod_inv_stmt(self, ctx: D96Parser.Method_inv_stmtContext):
        obj, method, param = self.visit(ctx.member_access_method())
        return [CallStmt(obj, method, param)]

    # Visit a parse tree produced by D96Parser#new_stmt.
    def visitNew_stmt(self, ctx: D96Parser.New_stmtContext):
        id = Id(ctx.ID().getText())
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        return [NewExpr(id, list_expr)]

    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.expr1(1):
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            op = '==.'
            if ctx.ADD_STRING():
                op = '+.'
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr1(0))

    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.expr2(1):
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            op = '=='
            if ctx.NOT_EQ_COMPARE():
                op = '!='
            elif ctx.SMALLER():
                op = '<'
            elif ctx.GREATER():
                op = '>'
            elif ctx.GR_OR_EQ():
                op = '>='
            elif ctx.SM_OR_EQ():
                op = '<='
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr2(0))

    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.expr2():
            op = '&&'
            if ctx.OR_():
                op = '||'
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.expr3():
            op = '+'
            if ctx.MINUS_():
                op = '-'
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.expr4():
            op = '*'
            if ctx.DIV_():
                op = '/'
            elif ctx.MOD_():
                op = '%'
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op, left, right)
        return self.visit(ctx.expr5())

    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        body = self.visit(ctx.expr5())
        return UnaryOp('!', body)

    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        body = self.visit(ctx.expr6())
        return UnaryOp('-', body)

    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.index_op():
            arr = self.visit(ctx.expr8())
            idx = self.visit(ctx.index_op())
            return ArrayCell(arr, idx)
        return self.visit(ctx.expr8())

    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.expr9():
            return self.visit(ctx.expr9())
        first = self.visit(ctx.expr8())
        second = Id(ctx.ID().getText())
        if ctx.LB():  # If it is a Static method
            list_expr = []
            if ctx.list_expr():
                list_expr = self.visit(ctx.list_expr())
            return CallExpr(first, second, list_expr)
        # If it is normal attribute access
        return FieldAccess(first, second)

    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.expr10():
            return self.visit(ctx.expr10())
        first = Id(ctx.ID().getText())
        second = Id(ctx.DOLLAR_ID().getText())
        if ctx.LB():  # If it is a Static method
            list_expr = []
            if ctx.list_expr():
                list_expr = self.visit(ctx.list_expr())
            return CallExpr(first, second, list_expr)
        # If it is normal attribute access
        return FieldAccess(first, second)

    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.primary():
            return self.visit(ctx.primary())
        id = Id(ctx.ID().getText())
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        return NewExpr(id, list_expr)

    # Visit a parse tree produced by D96Parser#primary.
    def visitPrimary(self, ctx: D96Parser.PrimaryContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.INT2():
            return IntLiteral(text2int(ctx.INT2().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.literal())
        # Return literal

    # Visit a parse tree produced by D96Parser#list_expr.
    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        return [self.visit(i) for i in ctx.expr()]
        # Return [Expr(), Expr(), ]

    # Visit a parse tree produced by D96Parser#index_op.
    def visitIndex_op(self, ctx: D96Parser.Index_opContext):
        return [self.visit(i) for i in ctx.expr()]
        # Return [Expr(), Expr(), ]

    # Visit a parse tree produced by D96Parser#member_access_attribute.
    def visitMember_access_attribute(self, ctx: D96Parser.Member_access_attributeContext):
        id = Id(ctx.ID().getText())
        if ctx.expr8():
            expr8 = self.visit(ctx.expr8())
            return FieldAccess(expr8, id)
        dollar_id = Id(ctx.DOLLAR_ID().getText())
        return FieldAccess(id, dollar_id)
        # Return a.a or a::$a

    # Visit a parse tree produced by D96Parser#member_access_method.
    def visitMember_access_method(self, ctx: D96Parser.Member_access_methodContext):
        list_expr = []
        if ctx.list_expr():
            list_expr = self.visit(ctx.list_expr())
        id = Id(ctx.ID().getText())
        if ctx.expr8():
            expr8 = self.visit(ctx.expr8())
            return expr8, id, list_expr
        dollar_id = Id(ctx.DOLLAR_ID().getText())
        return id, dollar_id, list_expr

        # Visit a parse tree produced by D96Parser#literal.

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INT():
            return IntLiteral(text2int(ctx.INT().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText() == 'True')
        elif ctx.FLOAT():
            return FloatLiteral(text2float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        return self.visit(ctx.iarray())
        # Return Literal or expression

    # Visit a parse tree produced by D96Parser#farray.
    def visitFarray(self, ctx: D96Parser.FarrayContext):
        return self.visit(ctx.getChild(0))
        # Visit int_array, float_array ...

    def visitInt_int2(self, ctx: D96Parser.Int_int2Context):
        return IntLiteral(text2int(ctx.getChild(0).getText()))

    # Visit a parse tree produced by D96Parser#int_array.
    def visitInt_array(self, ctx: D96Parser.Int_arrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.int_int2()])

    # Visit a parse tree produced by D96Parser#float_array.
    def visitFloat_array(self, ctx: D96Parser.Float_arrayContext):
        return ArrayLiteral([FloatLiteral(text2float(i.getText())) for i in ctx.FLOAT()])

    # Visit a parse tree produced by D96Parser#string_array.
    def visitString_array(self, ctx: D96Parser.String_arrayContext):
        return ArrayLiteral([StringLiteral(i.getText()) for i in ctx.STRING()])

    # Visit a parse tree produced by D96Parser#boolean_array.
    def visitBoolean_array(self, ctx: D96Parser.Boolean_arrayContext):
        return ArrayLiteral([BooleanLiteral(i.getText() == 'True') for i in ctx.BOOLEAN()])

    # Visit a parse tree produced by D96Parser#iarray.
    def visitIarray(self, ctx: D96Parser.IarrayContext):
        return self.visit(ctx.getChild(0))  # Visit the child iarray, farray

    # Visit a parse tree produced by D96Parser#marray.
    def visitMarray(self, ctx: D96Parser.MarrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.iarray()])  # Return [iarray, iarray,...]

    def visitExpr_array(self, ctx: D96Parser.Expr_arrayContext):
        return ArrayLiteral([self.visit(i) for i in ctx.expr()])
