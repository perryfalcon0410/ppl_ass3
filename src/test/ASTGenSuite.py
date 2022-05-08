import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """Class main { }"""
        expect = str(Program([ClassDecl(Id("main"), [])]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """Class main { } Class main2 {}"""
        expect = str(Program([ClassDecl(Id("main"), []), ClassDecl(Id("main2"), [])]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """Class main {} Class main2 : main {}"""
        expect = str(Program([ClassDecl(Id("main"), []), ClassDecl(Id("main2"), [], Id("main"))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """Class Program { main() {}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([]))])]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """Class Program { main() {Val a:Int;}}"""
        expect = str(Program(
            [ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([ConstDecl(Id('a'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """Class Program { main() {Val a,b:Int;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block(
            [ConstDecl(Id('a'), IntType()), ConstDecl(Id('b'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """Class Program { main() {Val a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [
            MethodDecl(Static(), Id("main"), [], Block([ConstDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """Class Program { main() {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block(
            [ConstDecl(Id('a'), IntType(), IntLiteral(2)), ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """Class Program { main() {Var a:Int;}}"""
        expect = str(Program(
            [ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([VarDecl(Id('a'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """Class Program { main() {Var a,b:Int;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [
            MethodDecl(Static(), Id("main"), [], Block([VarDecl(Id('a'), IntType()), VarDecl(Id('b'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """Class Program { main() {Var a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [
            MethodDecl(Static(), Id("main"), [], Block([VarDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """Class Program { main() {Var a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block(
            [VarDecl(Id('a'), IntType(), IntLiteral(2)), VarDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """Class Program { main() {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block(
            [ConstDecl(Id('a'), IntType(), IntLiteral(2)), ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """Class Rectangle {Var length: Int;}"""
        expect = str(
            Program([ClassDecl(Id("Rectangle"), [AttributeDecl(Instance(), VarDecl(Id("length"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """Class Rectangle {Val length: Int;}"""
        expect = str(
            Program([ClassDecl(Id("Rectangle"), [AttributeDecl(Instance(), ConstDecl(Id("length"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """Class Rectangle {Val $length: Int;}"""
        expect = str(
            Program([ClassDecl(Id("Rectangle"), [AttributeDecl(Static(), ConstDecl(Id("$length"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """Class Rectangle {Val $length: Int = 1;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
            AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """Class Rectangle {Val $length, $width: Int = 1, 2;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
                                        [AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(1))),
                                         AttributeDecl(Static(), ConstDecl(Id("$width"), IntType(), IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """Class Rectangle {Val $length, width: Int = 1, 2;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
                                        [AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(1))),
                                         AttributeDecl(Instance(),
                                                       ConstDecl(Id("width"), IntType(), IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """Class Rectangle {Val $length: Int = 0x123;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
            AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(0x123)))])]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """Class Rectangle {Val $length: Int = 0b1101;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
            AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(0b1101)))])]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """Class Rectangle {Val $length: Int = 01321;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
            AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(0o1321)))])]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """Class Rectangle {Val $length: Int = 01321; Val $width: String = "12";}"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
            AttributeDecl(Static(), ConstDecl(Id("$length"), IntType(), IntLiteral(0o1321))),
            AttributeDecl(Static(), ConstDecl(Id("$width"), StringType(), StringLiteral("12")))])]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """Class Program { notmain(a,b:Int) {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [
            MethodDecl(Instance(), Id("notmain"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())], Block(
                [ConstDecl(Id('a'), IntType(), IntLiteral(2)), ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """Class Program { notmain(a,b:Int; c:String) {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("notmain"),
                                                                   [VarDecl(Id("a"), IntType()),
                                                                    VarDecl(Id("b"), IntType()),
                                                                    VarDecl(Id("c"), StringType())], Block(
                [ConstDecl(Id('a'), IntType(), IntLiteral(2)), ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """Class Program { notmain(a,b:Int; c:String) {Val a,b:Int = 2,3;}notmain2(a:Int) {Val a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("notmain"),
                                                                   [VarDecl(Id("a"), IntType()),
                                                                    VarDecl(Id("b"), IntType()),
                                                                    VarDecl(Id("c"), StringType())], Block(
                [ConstDecl(Id('a'), IntType(), IntLiteral(2)), ConstDecl(Id('b'), IntType(), IntLiteral(3))])),
                                                        MethodDecl(Instance(), Id("notmain2"),
                                                                   [VarDecl(Id("a"), IntType())], Block(
                                                                [ConstDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                Return a;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Program"), [
            AttributeDecl(Static(), VarDecl(Id("$a"), StringType(), StringLiteral("haizz"))),
            MethodDecl(Instance(), Id("method"), [], Block([Return(Id("a"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                Break;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Program"), [
            AttributeDecl(Static(), VarDecl(Id("$a"), StringType(), StringLiteral("haizz"))),
            MethodDecl(Instance(), Id("method"), [], Block([Break()]))])]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                Continue;
                Return a;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Program"), [
            AttributeDecl(Static(), VarDecl(Id("$a"), StringType(), StringLiteral("haizz"))),
            MethodDecl(Instance(), Id("method"), [], Block([Continue(), Return(Id("a"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                a = 0;
                Return a;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Program"), [
            AttributeDecl(Static(), VarDecl(Id("$a"), StringType(), StringLiteral("haizz"))),
            MethodDecl(Instance(), Id("method"), [], Block([Assign(Id("a"), IntLiteral(0)), Return(Id("a"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                a.a = 0;
                Return a;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Program"), [
            AttributeDecl(Static(), VarDecl(Id("$a"), StringType(), StringLiteral("haizz"))),
            MethodDecl(Instance(), Id("method"), [],
                       Block([Assign(FieldAccess(Id("a"), Id("a")), IntLiteral(0)), Return(Id("a"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                a::$a = 0;
                Return a;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              StringType(),
                              StringLiteral("haizz"))),
                          MethodDecl(
                              Instance(),
                              Id("method"),
                              [],
                              Block([
                                  Assign(
                                      FieldAccess(
                                          Id("a"),
                                          Id("$a")),
                                      IntLiteral(0)),
                                  Return(
                                      Id("a"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """
        Class Program {
            Var $a: String = "haizz";
            method() {
                a.a();
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              StringType(),
                              StringLiteral("haizz"))),
                          MethodDecl(
                              Instance(),
                              Id("method"),
                              [],
                              Block([
                                  CallStmt(Id("a"), Id("a"), [])
                              ]))])]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """
        Class Program {
            Var $a: Array[Int, 5];
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              ArrayType(5, IntType())))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """
        Class Program {
            Var $a: Array[String, 5] = Array("sd","sd","ls","kl","ew");
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              ArrayType(5, StringType()),
                              ArrayLiteral([StringLiteral("sd"),
                                            StringLiteral("sd"),
                                            StringLiteral("ls"),
                                            StringLiteral("kl"),
                                            StringLiteral("ew")])))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """
        Class Program {
            Var $a: Int = 1 + 1;
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              IntType(),
                              BinaryOp(
                                  "+",
                                  IntLiteral(1),
                                  IntLiteral(1)
                              )
                          )
                      )
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """
        Class Program {
            Var $a: Array[Array[Int, 1], 2] = Array(Array(1), Array(1));
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              ArrayType(2, ArrayType(1, IntType())),
                              ArrayLiteral([ArrayLiteral([IntLiteral(1)]),
                                            ArrayLiteral([IntLiteral(1)])])))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """
        Class Program {
            Var $a: Array[Array[Array[Int, 1], 1], 2] = Array(Array(Array(1)), Array(Array(1)));
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [AttributeDecl(
                          Static(),
                          VarDecl(
                              Id("$a"),
                              ArrayType(2, ArrayType(1, ArrayType(1, IntType()))),
                              ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])]),
                                            ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """
        Class Program {
            method() {
                If 1 == 2 {
                    Return True;
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([If(BinaryOp("==", IntLiteral(1), IntLiteral(2)),
                                               Block([Return(BooleanLiteral(True))]))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """
        Class Program {
            method() {
                a = 1 == 2;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([Assign(Id("a"), BinaryOp("==", IntLiteral(1), IntLiteral(2)))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """
        Class Program {
            method() {
                If 1 == 2 {
                    Return True;
                } Elseif (2 == 3) {
                    Return False;
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([If(BinaryOp("==", IntLiteral(1), IntLiteral(2)),
                                               Block([Return(BooleanLiteral(True))]),
                                               If(BinaryOp("==", IntLiteral(2), IntLiteral(3)),
                                                  Block([Return(BooleanLiteral(False))])))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """
        Class Program {
            method() {
                If 1 == 2 {
                    Return True;
                } Elseif (2 == 3) {
                    Return False;
                } Else {Return Null;}
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([If(BinaryOp("==", IntLiteral(1), IntLiteral(2)),
                                               Block([Return(BooleanLiteral(True))]),
                                               If(BinaryOp("==", IntLiteral(2), IntLiteral(3)),
                                                  Block([Return(BooleanLiteral(False))]),
                                                  Block([Return(NullLiteral())])))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """
        Class Program {
            method() {
                Foreach (mem In 1 .. 4 By 2) {}
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([For(Id("mem"), IntLiteral(1), IntLiteral(4), Block([]), IntLiteral(2))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """
        Class Program {
            method() {
                Foreach (mem In 1 .. 4) {}
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([For(Id("mem"), IntLiteral(1), IntLiteral(4), Block([]), IntLiteral(1))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """
        Class Program {
            method() {
                Foreach (mem In 1 .. 4) {}
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),
                      [
                          MethodDecl(Instance(),
                                     Id("method"),
                                     [],
                                     Block([For(Id("mem"), IntLiteral(1), IntLiteral(4), Block([]), IntLiteral(1))]))
                      ])]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """
        Class A{
            Constructor(ele, acc: String; x, y: Int){
               If(True){

               } Else {

               }
            }
            ## Skip this comment ##            

            a(super, hero, viet_nguyen: Int){}

            Destructor(){}
        }
        """
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[param(Id(ele),StringType),param(Id(acc),StringType),param(Id(x),IntType),param(Id(y),IntType)],Block([If(BooleanLit(True),Block([]),Block([]))])),MethodDecl(Id(a),Instance,[param(Id(super),IntType),param(Id(hero),IntType),param(Id(viet_nguyen),IntType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """
        Class Right__ {
            Var c,d,e:String;
            Var a: Array[Int, 0b100] = Array(1, 3, 4, 5);
        }
        """
        expect = """Program([ClassDecl(Id(Right__),[AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,VarDecl(Id(d),StringType)),AttributeDecl(Instance,VarDecl(Id(e),StringType)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(3),IntLit(4),IntLit(5)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = """
        Class __Right__ {
            method() {
                If (1 == -2) {
                    Return asd;
                }
                Elseif (2 == 3) {
                    Break;
                    Continue;
                    Return 0;
                }
                Else {
                    Return 233;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(__Right__),[MethodDecl(Id(method),Instance,[],Block([If(BinaryOp(==,IntLit(1),UnaryOp(-,IntLit(2))),Block([Return(Id(asd))]),If(BinaryOp(==,IntLit(2),IntLit(3)),Block([Break,Continue,Return(IntLit(0))]),Block([Return(IntLit(233))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """
        Class __Right__ {
            method() {
                Foreach (asd In Rz >= Izj::$AL() .. R6F * Ik) {
                    vFCy = N >= Izoj::$J7kbL();
                }
                Return Nonsense;
            }
        }
        """
        expect = "Program([ClassDecl(Id(__Right__),[MethodDecl(Id(method),Instance,[],Block([For(Id(asd),BinaryOp(>=,Id(Rz),CallExpr(Id(Izj),Id($AL),[])),BinaryOp(*,Id(R6F),Id(Ik)),IntLit(1),Block([AssignStmt(Id(vFCy),BinaryOp(>=,Id(N),CallExpr(Id(Izoj),Id($J7kbL),[])))])]),Return(Id(Nonsense))]))])])"
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """
        Class Error {
            Constructor(param: String) {}
        }
        """
        expect = "Program([ClassDecl(Id(Error),[MethodDecl(Id(Constructor),Instance,[param(Id(param),StringType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = """
        Class __CCDeSua__ {
            Var a: Int = 12.e23;
            method_Kokomi() {
                Self.a = 0x333A;
            }
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FloatLit(1.2e+24))),MethodDecl(Id(method_Kokomi),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(13114))]))])])"
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = """
        Class __CCDeSua__ {
            Var a: Int = 12.e23;
            method_Kokomi() {
                a = Self + Self;
            }
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FloatLit(1.2e+24))),MethodDecl(Id(method_Kokomi),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Self(),Self()))]))])])"
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """
        Class __CCDeSua__ {
            Var a: Int = 12.e23;
            method_() {
                a::$foo();
            }
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FloatLit(1.2e+24))),MethodDecl(Id(method_),Instance,[],Block([Call(Id(a),Id($foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """
        Class __CCDeSua__ {
            Var a: Int = 12.e23;
            method_() {
                a[123]["ss"][1 + "192"] = Array(add, "sss");
            }
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FloatLit(1.2e+24))),MethodDecl(Id(method_),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(123),StringLit(ss),BinaryOp(+,IntLit(1),StringLit(192))]),[Id(add),StringLit(sss)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """
        Class __CCDeSua__ {
            Var a: Int = 12.e23;
            method_() {
                a[123]["ss"][1 + "233"] = New Y();
            }
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FloatLit(1.2e+24))),MethodDecl(Id(method_),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(123),StringLit(ss),BinaryOp(+,IntLit(1),StringLit(233))]),NewExpr(Id(Y),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """
        Class __CCDeSua__ {
            Var a: Int = 12.e23;
            method_() {
                a[123]["ss"][1 + "194"] = New X(Array(id0)).Y(333);
            }
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FloatLit(1.2e+24))),MethodDecl(Id(method_),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(123),StringLit(ss),BinaryOp(+,IntLit(1),StringLit(194))]),CallExpr(NewExpr(Id(X),[[Id(id0)]]),Id(Y),[IntLit(333)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """
        Class __CCDeSua__ {
            method() {
                a = Yashahime.parent1;
                b = Yashahime::$parent2;
            }
        }

        Class Yashahime {
            Var $num_of_hime: Int = 3;
            Var parent1, parent2: String = "Inuyasha", "Inusaga";
        }
        """
        expect = "Program([ClassDecl(Id(__CCDeSua__),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),FieldAccess(Id(Yashahime),Id(parent1))),AssignStmt(Id(b),FieldAccess(Id(Yashahime),Id($parent2)))]))]),ClassDecl(Id(Yashahime),[AttributeDecl(Static,VarDecl(Id($num_of_hime),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(parent1),StringType,StringLit(Inuyasha))),AttributeDecl(Instance,VarDecl(Id(parent2),StringType,StringLit(Inusaga)))])])"
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """
        Class mQhl0yb9Y1T5EvrBiQex {
            woWmo() {
                MGWDe = eOD * H8OD9;                    
                }
            Var bP2wG: String;
        }


        Class Yashahime {
            Var $num_of_hime: Int = 3;
            Var parent1, parent2: String = "Inuyasha", "Inusaga";
        }
        """
        expect = "Program([ClassDecl(Id(mQhl0yb9Y1T5EvrBiQex),[MethodDecl(Id(woWmo),Instance,[],Block([AssignStmt(Id(MGWDe),BinaryOp(*,Id(eOD),Id(H8OD9)))])),AttributeDecl(Instance,VarDecl(Id(bP2wG),StringType))]),ClassDecl(Id(Yashahime),[AttributeDecl(Static,VarDecl(Id($num_of_hime),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(parent1),StringType,StringLit(Inuyasha))),AttributeDecl(Instance,VarDecl(Id(parent2),StringType,StringLit(Inusaga)))])])"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """
        Class ooHOMDMd {
            C_uxURW5_zJ4g() {
                Gl2W = FZDM >= 42276318;
                Return a;
            }
            Var FeNMBk2v_: Float;
        }
        """
        expect = "Program([ClassDecl(Id(ooHOMDMd),[MethodDecl(Id(C_uxURW5_zJ4g),Instance,[],Block([AssignStmt(Id(Gl2W),BinaryOp(>=,Id(FZDM),IntLit(42276318))),Return(Id(a))])),AttributeDecl(Instance,VarDecl(Id(FeNMBk2v_),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """
        Class ooHOMDMd {
            C_uxURW5_zJ4g() {
                a[b[1]][c][a.foo()] = 1;
            }
            Var FeNMBk2v_: Float;
        }
        """
        expect = "Program([ClassDecl(Id(ooHOMDMd),[MethodDecl(Id(C_uxURW5_zJ4g),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(1)]),Id(c),CallExpr(Id(a),Id(foo),[])]),IntLit(1))])),AttributeDecl(Instance,VarDecl(Id(FeNMBk2v_),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """
        Class as {
        $getNumOfShape() {
            If (a == (1+1) ){
                Var b,c:Boolean = True, "False";
            }
            Foreach (i In hh .. 100 By 2 + 4) {
                 Var a:Boolean = True;
            }
        }}
        """
        expect = "Program([ClassDecl(Id(as),[MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(==,Id(a),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(b),BoolType,BooleanLit(True)),VarDecl(Id(c),BoolType,StringLit(False))])),For(Id(i),Id(hh),IntLit(100),BinaryOp(+,IntLit(2),IntLit(4)),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """
        Class as {
            PPL___(){
                methoda = "a" +. "aaaa" == "d22222";
            }
        }
        """
        expect = "Program([ClassDecl(Id(as),[MethodDecl(Id(PPL___),Instance,[],Block([AssignStmt(Id(methoda),BinaryOp(+.,StringLit(a),BinaryOp(==,StringLit(aaaa),StringLit(d22222))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
        Class as {
            PPL___(){

            }
            fooaaa() {
                    If (1) {}
                    b=1+-1;
                }
        }
        """
        expect = "Program([ClassDecl(Id(as),[MethodDecl(Id(PPL___),Instance,[],Block([])),MethodDecl(Id(fooaaa),Instance,[],Block([If(IntLit(1),Block([])),AssignStmt(Id(b),BinaryOp(+,IntLit(1),UnaryOp(-,IntLit(1))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """
        Class Animal {
            Var __id__: String;
        }

        Class Dog {
            bark() {
                Foreach (ss In 2 .. 4) {
                    Out.print();
                }}
        }
        """
        expect = "Program([ClassDecl(Id(Animal),[AttributeDecl(Instance,VarDecl(Id(__id__),StringType))]),ClassDecl(Id(Dog),[MethodDecl(Id(bark),Instance,[],Block([For(Id(ss),IntLit(2),IntLit(4),IntLit(1),Block([Call(Id(Out),Id(print),[])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """
            Class VioletEvergarden{
                main(){
                    Dying.out(a[i+2022-449/1212][i][j][h][k]);
                    test_26am = (1*1223.e100 * 3).getYou();
                }
            }
            """
        expect = "Program([ClassDecl(Id(VioletEvergarden),[MethodDecl(Id(main),Instance,[],Block([Call(Id(Dying),Id(out),[ArrayCell(Id(a),[BinaryOp(-,BinaryOp(+,Id(i),IntLit(2022)),BinaryOp(/,IntLit(449),IntLit(1212))),Id(i),Id(j),Id(h),Id(k)])]),AssignStmt(Id(test_26am),CallExpr(BinaryOp(*,BinaryOp(*,IntLit(1),FloatLit(1.223e+103)),IntLit(3)),Id(getYou),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:String = "em met khi code luc 3h sang";
            }
            foo(){
                Return True;
            }
        }
        Class Vehicle{
            run(){
                Self.playing = True;
            }
            stop(){
                Self.swimming = False;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(em met khi code luc 3h sang))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True))]))]),ClassDecl(Id(Vehicle),[MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(playing)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(swimming)),BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:String = "bai tap lon PPL nang qua hoa ra day la mon student killer";
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(bai tap lon PPL nang qua hoa ra day la mon student killer))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:String = "Spring di ngu that tuyet voi";
            }
            foo(){
                Return True;
                a = New Bugggggg();
                Buggggggg = Null;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(Spring di ngu that tuyet voi))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),NewExpr(Id(Bugggggg),[])),AssignStmt(Id(Buggggggg),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:String = "Em muon gap lai ban be";
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(Em muon gap lai ban be))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:Int = 213 - 233;
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),IntType,BinaryOp(-,IntLit(213),IntLit(233)))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:Int = 213 + 233;
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),IntType,BinaryOp(+,IntLit(213),IntLit(233)))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:Int = 213 / 233;
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),IntType,BinaryOp(/,IntLit(213),IntLit(233)))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1: Int = 33 % 11;
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),IntType,BinaryOp(%,IntLit(33),IntLit(11)))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                a[23] = 233;
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(23)]),IntLit(233))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                a::$foo();
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([Call(Id(a),Id($foo),[])])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:String = "lam ve sinh nha";
            }
            foo(){
                Return True;
                Break;
                Return aa;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(lam ve sinh nha))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),Break,Return(Id(aa))]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """
        Class Program{
            Val a: Int = 0;
            main(){
                Var var1:String = "Internet Explorer";
            }
            foo(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        Class Hyndai {}
        Class Toyota {}
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(Internet Explorer))])),MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))]),ClassDecl(Id(Hyndai),[]),ClassDecl(Id(Toyota),[])])"
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """
        Class _{Var $W7,_,t,$_:j_B_;}
        Class o__{}
        Class c_Cu:__q_{Var $__:Array [Array [Array [Float ,0XAB_2],3],06];Destructor (){} }
        Class AWt_{}"""
        expect = "Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($W7),ClassType(Id(j_B_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(j_B_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(t),ClassType(Id(j_B_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(j_B_)),NullLiteral()))]),ClassDecl(Id(o__),[]),ClassDecl(Id(c_Cu),Id(__q_),[AttributeDecl(Static,VarDecl(Id($__),ArrayType(6,ArrayType(3,ArrayType(2738,FloatType))))),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(AWt_),[])])"
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
        Class Program{
            Val a: Int = 0;
            oldschool(){
                Var var1: my_class;
            }
            nike(){
                Return True;
                a = Array(Array(2121, 2112));
            }
        }
        Class Hyndai {}
        Class Toyota {}"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(oldschool),Instance,[],Block([VarDecl(Id(var1),ClassType(Id(my_class)),NullLiteral())])),MethodDecl(Id(nike),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),[[IntLit(2121),IntLit(2112)]])]))]),ClassDecl(Id(Hyndai),[]),ClassDecl(Id(Toyota),[])])"
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """
        Class Program{
            Val a: Int = 0;
            longtime(){
                Var var1: my_class = 1;
            }
            ago(){
                Return True;
                a = a[2][3][4];
            }
        }
        Class LA0610 {}
        Class LT2711 {}"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(longtime),Instance,[],Block([VarDecl(Id(var1),ClassType(Id(my_class)),IntLit(1))])),MethodDecl(Id(ago),Instance,[],Block([Return(BooleanLit(True)),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(2),IntLit(3),IntLit(4)]))]))]),ClassDecl(Id(LA0610),[]),ClassDecl(Id(LT2711),[])])"
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """
        Class Program{
            Program() {
                Var a: Str = aString.toString();
            }
        }
        Class MiniMainiBurn {}
        Class Annie {}"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Program),Instance,[],Block([VarDecl(Id(a),ClassType(Id(Str)),CallExpr(Id(aString),Id(toString),[]))]))]),ClassDecl(Id(MiniMainiBurn),[]),ClassDecl(Id(Annie),[])])"
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """
        Class Program{
            Program() {
                i.Iwillcallyou();
                am.Atmidnight();
                dra.to();
                cu.suck();
                la.your();
                blah.blood();
                blah.dear();
                blah.Dracular();
            }
        }
        Class MiniMainiBurn {}
        Class Annie {}"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Program),Instance,[],Block([Call(Id(i),Id(Iwillcallyou),[]),Call(Id(am),Id(Atmidnight),[]),Call(Id(dra),Id(to),[]),Call(Id(cu),Id(suck),[]),Call(Id(la),Id(your),[]),Call(Id(blah),Id(blood),[]),Call(Id(blah),Id(dear),[]),Call(Id(blah),Id(Dracular),[])]))]),ClassDecl(Id(MiniMainiBurn),[]),ClassDecl(Id(Annie),[])])"
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """
        Class Program{
            Program() {
                Var a: Hey;
                Var b: Pickupthephone;
                Var a: Hey = nicetosuckyou;
            }
        }
        Class Hey {}
        Class Pickupthephone {}"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Program),Instance,[],Block([VarDecl(Id(a),ClassType(Id(Hey)),NullLiteral()),VarDecl(Id(b),ClassType(Id(Pickupthephone)),NullLiteral()),VarDecl(Id(a),ClassType(Id(Hey)),Id(nicetosuckyou))]))]),ClassDecl(Id(Hey),[]),ClassDecl(Id(Pickupthephone),[])])"
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """
        Class Program{
            main(a: Int) {
                If (a == convert.toInt("dream")) {
                    Change.invoke();
                } Elseif (a == 2) {
                    Girlfriend.add();
                }
            }
        }
        Class MLP {}"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,Id(a),CallExpr(Id(convert),Id(toInt),[StringLit(dream)])),Block([Call(Id(Change),Id(invoke),[])]),If(BinaryOp(==,Id(a),IntLit(2)),Block([Call(Id(Girlfriend),Id(add),[])])))]))]),ClassDecl(Id(MLP),[])])"
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """
        Class Program{
            main(a: Int) {
                If (a == convert.toInt("dream")) {
                    Change.invoke();
                } Elseif (a == 2) {
                    Girlfriend.add();
                } Else {
                    sweaty_peach = a;
                    Return you;
                }
            }
        }
        Class MLP {
            khongemthiaimain() {
                Return Dell;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,Id(a),CallExpr(Id(convert),Id(toInt),[StringLit(dream)])),Block([Call(Id(Change),Id(invoke),[])]),If(BinaryOp(==,Id(a),IntLit(2)),Block([Call(Id(Girlfriend),Id(add),[])]),Block([AssignStmt(Id(sweaty_peach),Id(a)),Return(Id(you))])))]))]),ClassDecl(Id(MLP),[MethodDecl(Id(khongemthiaimain),Instance,[],Block([Return(Id(Dell))]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """
        Class attach{

        }
        Class attach{

        }
        """
        expect = "Program([ClassDecl(Id(attach),[]),ClassDecl(Id(attach),[])])"
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """
        Class dem_ngay_testcase{
            Var a: Int = !!!!!!!!!!!!!!!!!1;
        }"""
        expect = "Program([ClassDecl(Id(dem_ngay_testcase),[AttributeDecl(Instance,VarDecl(Id(a),IntType,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1))))))))))))))))))))])])"
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """
        Class dem_ngay_testcase{
            Var a: Int = --------------------1;
        }"""
        expect = "Program([ClassDecl(Id(dem_ngay_testcase),[AttributeDecl(Instance,VarDecl(Id(a),IntType,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))))))))))))))))))))])])"
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """
        Class dem_ngay_testcase{
            Var a: String = "day la 1 bai hat vui";
        }"""
        expect = "Program([ClassDecl(Id(dem_ngay_testcase),[AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(day la 1 bai hat vui)))])])"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """
        Class dem_ngay_testcase{
            Var a: String = "day la 1 bai hat khong buon";
            Var b: String = "day la 1 bai hat rat rat vui";
            Var c: String = "";
        }"""
        expect = "Program([ClassDecl(Id(dem_ngay_testcase),[AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(day la 1 bai hat khong buon))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(day la 1 bai hat rat rat vui))),AttributeDecl(Instance,VarDecl(Id(c),StringType,StringLit()))])])"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """
        Class dem_ngay_testcase{
            Constructor() {dem_nay.aDestructor();}
            Destructor() {}
        }"""
        expect = "Program([ClassDecl(Id(dem_ngay_testcase),[MethodDecl(Id(Constructor),Instance,[],Block([Call(Id(dem_nay),Id(aDestructor),[])])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """
        Class homnay_lam_dc_30test{
            Var a: Int = "sap duoc nghi roi";
            method(get: Int) {}
        }"""
        expect = "Program([ClassDecl(Id(homnay_lam_dc_30test),[AttributeDecl(Instance,VarDecl(Id(a),IntType,StringLit(sap duoc nghi roi))),MethodDecl(Id(method),Instance,[param(Id(get),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;
        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;

            add(value: Int) {
                Self.arr[Self.len] = value;
                Self.len = Self.len + 1;
            }

        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(value),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(len))]),Id(value)),AssignStmt(FieldAccess(Self(),Id(len)),BinaryOp(+,FieldAccess(Self(),Id(len)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;

            add(value: Int) {
                Self.arr[Self.len] = value;
                Self.len = Self.len + 1;
            }

            sort_1() {
                Foreach (i In 0 .. Self.len) {
                    Foreach (j In i + 1 .. Self.len) {
                        If (Self.arr[i] > Self.arr[j]) {
                            lib.swap(Self.arr[i], Self.arr[j]);
                        }
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(value),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(len))]),Id(value)),AssignStmt(FieldAccess(Self(),Id(len)),BinaryOp(+,FieldAccess(Self(),Id(len)),IntLit(1)))])),MethodDecl(Id(sort_1),Instance,[],Block([For(Id(i),IntLit(0),FieldAccess(Self(),Id(len)),IntLit(1),Block([For(Id(j),BinaryOp(+,Id(i),IntLit(1)),FieldAccess(Self(),Id(len)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(FieldAccess(Self(),Id(arr)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(j)])),Block([Call(Id(lib),Id(swap),[ArrayCell(FieldAccess(Self(),Id(arr)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(j)])])]))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;

            add(value: Int) {
                Self.arr[Self.len] = value;
                Self.len = Self.len + 1;
            }

            sort_1() {
                Foreach (i In 0 .. Self.len) {
                    Foreach (j In i + 1 .. Self.len) {
                        If (Self.arr[i] <= Self.arr[j]) {
                            lib.swap(Self.arr[i], Self.arr[j]);
                        }
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(value),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(len))]),Id(value)),AssignStmt(FieldAccess(Self(),Id(len)),BinaryOp(+,FieldAccess(Self(),Id(len)),IntLit(1)))])),MethodDecl(Id(sort_1),Instance,[],Block([For(Id(i),IntLit(0),FieldAccess(Self(),Id(len)),IntLit(1),Block([For(Id(j),BinaryOp(+,Id(i),IntLit(1)),FieldAccess(Self(),Id(len)),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(FieldAccess(Self(),Id(arr)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(j)])),Block([Call(Id(lib),Id(swap),[ArrayCell(FieldAccess(Self(),Id(arr)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(j)])])]))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;

            add(value: Int) {
                Self.arr[Self.len] = value;
                Self.len = Self.len + 1;
            }

            sort_2() {
                Foreach (i In 0 .. Self.len) {
                    Var pos: Int = 0;
                    Foreach (j In Self.len .. i + 1 By -1) {
                        If ((Self.arr[i] < Self.arr[j]) && (Self.arr[i - 1] < Self.arr[j])) {
                            pos = j;
                        }
                    }
                    lib.swap(Self.arr[i], Self.arr[pos]);
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(value),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(len))]),Id(value)),AssignStmt(FieldAccess(Self(),Id(len)),BinaryOp(+,FieldAccess(Self(),Id(len)),IntLit(1)))])),MethodDecl(Id(sort_2),Instance,[],Block([For(Id(i),IntLit(0),FieldAccess(Self(),Id(len)),IntLit(1),Block([VarDecl(Id(pos),IntType,IntLit(0)),For(Id(j),FieldAccess(Self(),Id(len)),BinaryOp(+,Id(i),IntLit(1)),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(&&,BinaryOp(<,ArrayCell(FieldAccess(Self(),Id(arr)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(j)])),BinaryOp(<,ArrayCell(FieldAccess(Self(),Id(arr)),[BinaryOp(-,Id(i),IntLit(1))]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(j)]))),Block([AssignStmt(Id(pos),Id(j))]))])]),Call(Id(lib),Id(swap),[ArrayCell(FieldAccess(Self(),Id(arr)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(arr)),[Id(pos)])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;

            add(value: Int) {
                Self.arr[Self.len] = value;
                Self.len = Self.len + 1;
            }

            sort_2() {
                Array_l.sort_1();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(value),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(len))]),Id(value)),AssignStmt(FieldAccess(Self(),Id(len)),BinaryOp(+,FieldAccess(Self(),Id(len)),IntLit(1)))])),MethodDecl(Id(sort_2),Instance,[],Block([Call(Id(Array_l),Id(sort_1),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
        Class Array_decl {
            Var arr: Array[Int, 1000];
            Var len: Int = 0;

            add(value: Int) {
                Self.arr[Self.len] = value;
                Self.len = Self.len + 1;
            }

            sort_3() {
                Array_l.sort_2();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Array_decl),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,IntType))),AttributeDecl(Instance,VarDecl(Id(len),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(value),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(len))]),Id(value)),AssignStmt(FieldAccess(Self(),Id(len)),BinaryOp(+,FieldAccess(Self(),Id(len)),IntLit(1)))])),MethodDecl(Id(sort_3),Instance,[],Block([Call(Id(Array_l),Id(sort_2),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """
        Class last_test {
            Var Min: Girl = "A penguin";
            dress_in_JK() {
                Return perfect;
            }
            sleep(hour: Float) {
                If (hour < 2) {
                    hour = 24;
                }
            }
            luot_tiktok() {}
            luot_shopee() {}
            doi_doi() {}
            scary(a: Int) {
                a = 0;
            }
        }
        """
        expect = "Program([ClassDecl(Id(last_test),[AttributeDecl(Instance,VarDecl(Id(Min),ClassType(Id(Girl)),StringLit(A penguin))),MethodDecl(Id(dress_in_JK),Instance,[],Block([Return(Id(perfect))])),MethodDecl(Id(sleep),Instance,[param(Id(hour),FloatType)],Block([If(BinaryOp(<,Id(hour),IntLit(2)),Block([AssignStmt(Id(hour),IntLit(24))]))])),MethodDecl(Id(luot_tiktok),Instance,[],Block([])),MethodDecl(Id(luot_shopee),Instance,[],Block([])),MethodDecl(Id(doi_doi),Instance,[],Block([])),MethodDecl(Id(scary),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 399))




