
"""
 * @author nhphung
"""
from matplotlib.pyplot import cla
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class Check:
    def binCheck(ope: str, type1: Type, type2: Type, expr: Expr):
        # Operand type IntFloat return IntFloat
        arith = ['-', '+', '*', '/']
        arith_int = '%'
        # Operand type Boolean/String return Boolean
        bool_ = ['&&', '||', '==.']
        # Operand type String return String
        string_ = '+.'
        # Operand type IntFloat / IntBoolean return Boolean
        rela_op = ['==', '!=', '<', '>', '<=', '>=']
        if ope == arith_int:
            if type(type1) is IntType and type(type2) is IntType:
                return IntType()
        elif ope == string_:
            if type(type1) is StringType and type(type2) is StringType:
                return StringType()
        elif ope in arith:
            if type(type1) in [IntType, FloatType] and type(type2) in [IntType, FloatType]:
                if type(type1) is FloatType or type(type2) is FloatType:
                    return FloatType()
                else:
                    return IntType()
        elif ope in bool_:
            if ope == '==.':
                if type(type1) is StringType and type(type2) is StringType:
                    return BoolType()
            elif type(type1) is BoolType and type(type2) is BoolType:
                return BoolType()
        elif ope in rela_op:
            if ope in ['==', '!=']:
                if type(type1) in [BoolType, IntType] and type(type2) in [BoolType, IntType] and type(type1) is type(type2):
                    return BoolType()
            elif type(type1) in [FloatType, IntType] and type(type2) in [FloatType, IntType]:
                return BoolType()
        raise TypeMismatchInExpression(expr)
                
    def unCheck(ope: str, typ: Type, expr: Expr):
        if ope == '!':
            if typ is BoolType:              
                return BoolType()
        elif ope == '-':
            if typ in [IntType, FloatType]:
                return typ
        raise TypeMismatchInExpression(expr)

class Symbol: pass
class Scope: pass
class ScopedSymbol(Symbol, Scope): pass
class ClassSymbol(ScopedSymbol, Type): pass

# Static attribute and instance
# Refer to thing in class
class AttributeSymbol(Symbol):
    def __init__(self, name: str, type: Type, kind: SIKind, cv: Kind) -> None:
        self.name = name
        self.type = type        # IntType, FloatType
        self.kind = kind        # Static or Instance
        self.cv = cv            # Constant or variable
    
    def __str__(self) -> str:
        return "AttributeSymbol(" + str(self.name) + "," + str(self.type) + "," + str(self.kind) + "," + str(self.cv)+ ")"

# Refer to thing in method
class VariableSymbol(Symbol):
    def __init__(self, name: str, type: Type, cv: Kind) -> None:
        self.name = name
        self.type = type        # IntType, FloatType ...
        self.cv = cv          # Constant or variable or parameter
    
    def __str__(self) -> str:
        return "VariableSymbol(" + str(self.name) + "," + str(self.type) + "," + str(self.cv) + ")"

# IntType, Float, String, Boolean, Array and Class type
# are written in AST
class MethodSymbol(ScopedSymbol):
    def __init__(self, name: str, kind: SIKind, blockScope: Scope=None) -> None:
        self.name = name
        self.kind = kind
        self.symbols = []               # Store only the parameters
        self.blockScope = blockScope    # Use storing statement scope //// LATE INIT
        self.upperScope = None          # TODO: this use self. Look back the symbol in class Scope to find attribute
        self.insideClass = ""
        self.type = VoidType()
    
    def addSymbol(self, symbol: Symbol):
        self.symbols.append(symbol)

    def belongToClass(self, name: str):
        self.insideClass = name

    def trigger(self):
        self.blockScope.upperScope = self
    
    def typeInfer(self, type: Type):
        self.type = type
    
    def __str__(self) -> str:
        return "MethodSymbol(" + str(self.name) + "," + str(self.kind) + "," + str(len(self.symbols)) + ")"

class ClassSymbol(ScopedSymbol, Type):
    def __init__(self, name: str, type: Type, superClass: ClassSymbol=None) -> None:
        self.name = name
        self.type = type
        self.symbols = []
        self.superClass = superClass
    
    def addSymbol(self, symbol: Symbol):
        self.symbols.append(symbol)
    
    def allSymbols(self):
        super = self.superClass
        sym = self.symbols
        while super is not None:
            names = [i.name for i in sym]
            for i in super.symbols:
                # Dont need the previous declaration
                if i.name not in names:
                    sym.append(i)
            super = super.superClass
        return sym

    def __str__(self) -> str:
        return "ClassSymbol(" + str(self.name) + "," + str(self.type) + "," + str(len(self.symbols)) + "," + (self.superClass.name if self.superClass else "") + ")"

class GlobalScope(Scope):
    def __init__(self) -> None:
        self.symbols = []

    def addSymbol(self, symbol: Symbol) -> None:
        self.symbols.append(symbol)
    
    def __str__(self) -> str:
        return "GlobalScope(Global," + ','.join(str(i.name) for i in self.symbols) + ")"

class BlockScope(Scope):
    def __init__(self) -> None:
        self.symbols = []               # Store variable declaration in this scope Ex: For scope
        self.blockScope = []            # Reference if block scope have if statement or for statement
        self.upperScope = None          # Referenec to upperScope
    
    def addSymbol(self, symbol: Symbol):
        self.symbols.append(symbol)
    
    def addBlock(self, block: Scope):
        self.blockScope.append(block)
    
    def getToMethod(self):
        upper = self
        while upper.upperScope is not None:
            upper = upper.upperScope
        return upper
    
    def lookUpperPlease(self) -> List[Symbol]:
        sym = self.symbols
        upper = self.upperScope
        while upper is not None:
            names = [i.name for i in sym]
            for i in upper.symbols:
                # Dont need the previous declaration cause messing with type
                if i.name not in names:
                    sym.append(i)
            upper = upper.upperScope
        return sym
    
    def trigger(self) -> None:
        if self.blockScope != []:
            for i in self.blockScope:
                i.upperScope = self

    def lookClass(self):
        upper = self.upperScope
        while upper.upperScope is not None:
            upper = upper.upperScope
        return upper.insideClass
        
    
    def __str__(self) -> str:
        return "BlockScope(Block," + ','.join(str(i.name) for i in self.symbols) + (",Upper" if self.upperScope else "") + ")"

class StaticChecker(BaseVisitor,Utils):
    root = GlobalScope()

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        x = None
        for i in self.ast.decl:
            if i.classname.name == "Program":
                x = i
                break
        if x is None:
            raise NoEntryPoint()
        y = None
        for i in x.memlist:
            if type(i) is MethodDecl and i.name.name == 'main':
                y = i
                break
        if y is None:
            raise NoEntryPoint()
        return self.visit(self.ast, StaticChecker.root)
        
    def visitProgram(self, ast: Program, c):
        for i in ast.decl:
            self.visit(i, c)

    def visitClassDecl(self, ast: ClassDecl, c: GlobalScope):
        # Declare, Check redeclare, super class undeclared and add symbols
        typ = ClassType(ast.classname.name)
        if self.lookup(ast.classname.name, c.symbols, lambda x: x.name) is not None:
            raise Redeclared(Class(), ast.classname.name)
        superClass = None
        if ast.parentname is not None:
            superClass = self.lookup(ast.parentname.name, c.symbols, lambda x: x.name)
            if superClass is None:
                raise Undeclared(Class(), ast.parentname.name)            
        x = ClassSymbol(ast.classname.name, typ, superClass)
        c.addSymbol(x)
        for i in ast.memlist:
            self.visit(i, {'upper': x})
        if 'Constructor' not in str(ast):
            x.addSymbol(MethodSymbol('Constructor', Instance(), BlockScope()))
    
    def visitAttributeDecl(self, ast: AttributeDecl, c):
        classSymbol = c["upper"]
        name, varType, kind = self.visit(ast.decl, ast)
        for i in classSymbol.symbols:
            if name == i.name:
                raise Redeclared(Attribute(), name)
        classSymbol.addSymbol(AttributeSymbol(name, varType, ast.kind, kind))
           
    def visitMethodDecl(self, ast: MethodDecl, c):
        classSymbol = c["upper"]
        for i in classSymbol.symbols:
            if ast.name == i.name:
                raise Redeclared(Method(), ast.name)
        y = MethodSymbol(ast.name.name, ast.kind)
        for i in ast.param:
            for j in y.symbols:
                if i.variable.name == j.name:
                    raise Redeclared(Parameter(), j.name)
            y.addSymbol(VariableSymbol(i.variable.name, i.varType, Parameter()))
        # Visit block
        y.blockScope = BlockScope()
        y.trigger()
        y.belongToClass(classSymbol.name)
        classSymbol.addSymbol(y)
        self.visit(ast.body, {"belongToFor": False, "upper": y, 'block_pos': -1})        
        
    def visitVarDecl(self, ast: VarDecl, c):
        # TODO: Check the varType and varInit
        if ast.varInit is not None:
            if self.visit(ast.varInit, c) != ast.varType:
                raise TypeMismatchInStatement(c)
        return ast.variable.name, ast.varType, Variable()

    def visitConstDecl(self, ast: ConstDecl, c):
        if ast.value is None:
            raise IllegalConstantExpression(None)
        # TODO: Check evaluate problem
        return ast.constant.name, ast.constType, Constant()
    
    def visitBlock(self, ast: Block, c):
        belong = c['belongToFor']
        upper = c['upper'] # Method or For If block

        if c['block_pos'] == -1:
            block = upper.blockScope # Only 1 blockScope for method
        else:
            block = upper.blockScope[c['block_pos']]

        for i in ast.inst:
            # Refresh the symbols
            symbols = block.symbols
            # symbols = block.lookUpperPlease()

            if type(i) is VarDecl:
                if self.lookup(i.variable.name, symbols, lambda x: x.name) is not None:
                    raise Redeclared(Variable(), i.variable.name)
                name, typ, var = self.visit(i, block)
                block.addSymbol(VariableSymbol(name, typ, var))
            elif type(i) is ConstDecl:
                if self.lookup(i.constant.name, symbols, lambda x: x.name) is not None:
                    raise Redeclared(Constant(), i.constant.name)
                name, typ, con = self.visit(i, block)
                block.addSymbol(VariableSymbol(name, typ, con))
            elif type(i) in [For, If, Block]:
                small_block = BlockScope()
                block.addBlock(small_block)
                block.trigger()
                self.visit(i, {'belongToFor': belong, 'upper': block, 'block_pos': len(block.blockScope) - 1})
            else:
            # Visit Assign, Return, Break, Continue, Callstmt
                self.visit(i, {'belongToFor': belong, 'upper': block})


    def visitBinaryOp(self, ast: BinaryOp, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        ope = ast.op
        return Check.binCheck(ope, left, right, ast)
    
    def visitUnaryOp(self, ast: UnaryOp, c):
        body_type = self.visit(ast.body, c)
        ope = ast.op
        return Check.unCheck(ope, body_type, ast)

    def visitCallExpr(self, ast: CallExpr, c):
        # 2 kind of self, and Id
        if type(ast.obj) is Id:
            obj = self.look_class_from_global(ast.obj.name)
        else:
        # Obj can be self
            obj = self.visit(ast.obj, c)
        method = self.lookup(ast.method.name, obj.allSymbols(), lambda x: x.name)
        if method is None:
            raise Undeclared(Method(), ast.method.name)
        if type(method.type) is VoidType or len(method.symbols) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        for i in range(len(method.symbols)):
            type_param_i = self.visit(ast.param[i], c)
            if self.compatibleAssign(method.symbols[i].type, type_param_i) is False:
                raise TypeMismatchInExpression(ast)
        return method.type
        
    def visitCallStmt(self, ast: CallStmt, c):
        # 2 kind of self, and Id
        if type(ast.obj) is Id:
            obj = self.look_class_from_global(ast.obj.name)
        else:
        # Obj can be self
            obj = self.visit(ast.obj, c)
        method = self.lookup(ast.method.name, obj.allSymbols(), lambda x: x.name)
        if method is None:
            raise Undeclared(Method(), ast.method.name)
        if type(method.type) is not VoidType or len(method.symbols) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        for i in range(len(method.symbols)):
            type_param_i = self.visit(ast.param[i], c)
            if self.compatibleAssign(method.symbols[i].type, type_param_i):
                raise TypeMismatchInStatement(ast)

    def visitNewExpr(self, ast: NewExpr, c):
        class_symbol = self.look_class_from_global(ast.classname)
        method = self.lookup('Constructor', class_symbol.symbols, lambda x: x.name)
        if len(method.symbols) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.param)):
            type_param_i = self.visit(ast.param[i], c)
            if self.compatibleAssign(method.symbols[i].type, type_param_i):
                raise TypeMismatchInStatement(ast)
        return ClassType(Id(ast.classname.name))
    
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        # TODO: rewrite array visit and check
        idx_type = self.visit(ast.value[0], c)
        for i in ast.value:
            if self.visit(i, c) != idx_type:
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(ast.value), idx_type)
   
    # Null type is need to initialize
    def visitNullLiteral(self, ast: NullLiteral, c):
        return VoidType()
    
    # Return the name of the class
    def visitSelfLiteral(self, ast: SelfLiteral, c):
        return self.look_class_from_global(c.lookClass())

    def visitAssign(self, ast: Assign, c):
        # 3 cases: Id case, ArrayCell, FieldAccess
        block = c['upper']
        lhs_type = self.visit(ast.lhs, block)
        if type(lhs_type) is VoidType:
            raise TypeMismatchInStatement(ast)
        rhs_type = self.visit(ast.exp, block)
        if self.compatibleAssign(lhs_type, rhs_type) is False:
            raise TypeMismatchInStatement(ast)
    
    def visitId(self, ast: Id, c):
        # Id visit here only look in the Scope symbol
        sym = c.lookUpperPlease()
        for i in sym:
            if i.name == ast.name:
                return i.type
        raise Undeclared(Identifier(), ast.name) 
    
    def visitArrayCell(self, ast: ArrayCell, c):
        arr = self.visit(ast.arr, c)
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for i in ast.idx:
            if self.visit(i, c) is not IntType:
                raise TypeMismatchInExpression(ast)
    
    def visitFieldAccess(self, ast: FieldAccess, c):
        # Obj can be Id which is classname
        # Both return class Symbol
        # TODO: illegal member access here
        if type(ast.obj) is Id:
            obj = self.look_class_from_global(ast.obj.name)
        else:
        # Obj can be self
            obj = self.visit(ast.obj, c)      
        for i in obj.allSymbols():
            if type(i) is AttributeSymbol and i.name == ast.fieldname.name:
                return i.type
             
    def visitFor(self, ast: For, c):
        upper_block = c['upper']
        this_block = upper_block.blockScope[c['block_pos']]
        if self.lookup(ast.id.name, this_block.lookUpperPlease(), lambda x: x.name) is None:
            raise Undeclared(Variable(), ast.id.name)
        if self.visit(ast.expr1, this_block) is not IntType and self.visit(ast.expr2, this_block) is not IntType:
            raise TypeMismatchInStatement(ast)
        if ast.expr3 is not None and self.visit(ast.expr3, this_block) is not IntType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, {'belongToFor': True, 'upper': this_block})

    def visitIf(self, ast: If, c):
        belong = c['belongToFor']
        if self.visit(ast.expr, c) is not BoolType:
            raise TypeMismatchInStatement(ast)
        upper_block = c['upper']
        this_block = upper_block.blockScope[c['block_pos']]
        self.visit(ast.thenStmt, {'belongToFor': belong, 'upper': this_block})
        if ast.elseStmt:
            self.visit(ast.elseStmt, {'belongToFor': belong, 'upper': this_block})

    def visitBreak(self, ast: Break, c):
        if c['forblock'] is False:
            raise MustInLoop(ast)

    def visitContinue(self, ast: Continue, c):
        if c['forblock'] is False:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, c):
        upper = c['upper']
        method = upper.getToMethod()
        if ast.expr is None:
            return VoidType()
        ret_type = self.visit(ast.expr, c)
        if type(method.type) is VoidType:
            method.typeInfer(ret_type)
        else:
            if type(ret_type) != type(method.type):
                raise TypeMismatchInStatement(ast)

    def visitIntLiteral(self, ast: IntLiteral, c):
        return IntType()  

    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return FloatType()   
         
    def visitStringLiteral(self, ast: StringLiteral, c):
        return StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return BoolType()       

    def look_class_from_global(self, classname: str) -> ClassSymbol:
        x = self.lookup(classname, StaticChecker.root.symbols, lambda x: x.name)
        # x is None mean that that class dont exist
        if x is None:
            raise Undeclared(Class(), classname)
        return x
    
    def class_coerce(self, class_: ClassType):
        type_accept = []
        x = self.look_class_from_global(class_.classname)
        while x.superClass is not None:
            type_accept.append(x.type)
        return type_accept
    
    def compatibleAssign(self, lhs: Type, rhs: Type):
        if type(lhs) is type(rhs):
            return True
        # Check IntFloat coerce, class Coerce
        if type(lhs) is FloatType and type(rhs) is IntType:
            return True        
        if type(rhs) is ClassType and type(lhs) in self.class_coerce(rhs):
            return True
        return False
    
# a = StaticChecker(Program([ClassDecl(Id("Rectangle"), [
#     #AttributeDecl(Instance(), VarDecl(Id("length"), IntType(), IntLiteral(1))), 
#     MethodDecl(Instance(),Id("name"),[VarDecl(Id("a"),IntType())], 
#     Block([
#         #Assign(FieldAccess(SelfLiteral(), Id("length")), IntLiteral(1)),
#         Assign(Id('a'), IntLiteral(1)), 
#         Return(IntLiteral(0)),
#         VarDecl(Id('b'), IntType(), BinaryOp('+', IntLiteral(5), IntLiteral(2))),
#         Block([
#             #Assign(FieldAccess(SelfLiteral(), Id("length")), IntLiteral(1)),
#             #Assign(Id('a'), IntLiteral(1)), 
#             #Assign(Id('b'), FieldAccess(SelfLiteral(), Id("length"))), 
#             Return(IntLiteral(0))

#         ])
#         ])),
#     MethodDecl(Instance(),Id("name1"),[VarDecl(Id("a"),IntType())], 
#     Block([
#         #Assign(FieldAccess(SelfLiteral(), Id("length")), IntLiteral(1)),
#         Assign(Id('a'), CallExpr(SelfLiteral(), Id('name'), [IntLiteral(1)])),
#         ])),
#     ])]))
# a.check()

a = StaticChecker(Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([]))])]))
a.check()