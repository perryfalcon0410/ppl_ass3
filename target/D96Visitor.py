# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_block.
    def visitClass_block(self, ctx:D96Parser.Class_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx:D96Parser.Class_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx:D96Parser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_1.
    def visitAttr_decl_1(self, ctx:D96Parser.Attr_decl_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_2.
    def visitAttr_decl_2(self, ctx:D96Parser.Attr_decl_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#extend_1.
    def visitExtend_1(self, ctx:D96Parser.Extend_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_type.
    def visitId_type(self, ctx:D96Parser.Id_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idList.
    def visitIdList(self, ctx:D96Parser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nor_id_type.
    def visitNor_id_type(self, ctx:D96Parser.Nor_id_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nor_idList.
    def visitNor_idList(self, ctx:D96Parser.Nor_idListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vari_decl_1.
    def visitVari_decl_1(self, ctx:D96Parser.Vari_decl_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vari_decl_2.
    def visitVari_decl_2(self, ctx:D96Parser.Vari_decl_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#extend_2.
    def visitExtend_2(self, ctx:D96Parser.Extend_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:D96Parser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeDeclaration2.
    def visitTypeDeclaration2(self, ctx:D96Parser.TypeDeclaration2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_param.
    def visitList_param(self, ctx:D96Parser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_decl.
    def visitParam_decl(self, ctx:D96Parser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_block.
    def visitStmt_block(self, ctx:D96Parser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_block_ret.
    def visitStmt_block_ret(self, ctx:D96Parser.Stmt_block_retContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vari_decl.
    def visitVari_decl(self, ctx:D96Parser.Vari_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#condition_block.
    def visitCondition_block(self, ctx:D96Parser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_block.
    def visitElseif_block(self, ctx:D96Parser.Elseif_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_blocks.
    def visitElseif_blocks(self, ctx:D96Parser.Elseif_blocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_block.
    def visitElse_block(self, ctx:D96Parser.Else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_each_stmt.
    def visitFor_each_stmt(self, ctx:D96Parser.For_each_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_inv_stmt.
    def visitMethod_inv_stmt(self, ctx:D96Parser.Method_inv_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#new_stmt.
    def visitNew_stmt(self, ctx:D96Parser.New_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primary.
    def visitPrimary(self, ctx:D96Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_expr.
    def visitList_expr(self, ctx:D96Parser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_op.
    def visitIndex_op(self, ctx:D96Parser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_attribute.
    def visitMember_access_attribute(self, ctx:D96Parser.Member_access_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_method.
    def visitMember_access_method(self, ctx:D96Parser.Member_access_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#farray.
    def visitFarray(self, ctx:D96Parser.FarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_array.
    def visitExpr_array(self, ctx:D96Parser.Expr_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_int2.
    def visitInt_int2(self, ctx:D96Parser.Int_int2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_array.
    def visitInt_array(self, ctx:D96Parser.Int_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_array.
    def visitFloat_array(self, ctx:D96Parser.Float_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_array.
    def visitString_array(self, ctx:D96Parser.String_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_array.
    def visitBoolean_array(self, ctx:D96Parser.Boolean_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#iarray.
    def visitIarray(self, ctx:D96Parser.IarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#marray.
    def visitMarray(self, ctx:D96Parser.MarrayContext):
        return self.visitChildren(ctx)



del D96Parser