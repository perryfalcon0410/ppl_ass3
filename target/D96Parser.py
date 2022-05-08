# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u029e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\6\2\u0088\n\2\r\2\16\2\u0089\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u0094\n\4\3\4\3\4\3\5\3\5\7\5\u009a\n\5\f")
        buf.write("\5\16\5\u009d\13\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u00a5\n")
        buf.write("\6\3\7\3\7\3\7\5\7\u00aa\n\7\3\b\3\b\3\b\5\b\u00af\n\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00b7\n\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d5")
        buf.write("\n\r\3\16\3\16\3\17\3\17\3\17\7\17\u00dc\n\17\f\17\16")
        buf.write("\17\u00df\13\17\3\20\3\20\3\21\3\21\3\21\7\21\u00e6\n")
        buf.write("\21\f\21\16\21\u00e9\13\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00ff\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u0107\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u010e\n\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0116")
        buf.write("\n\27\3\27\3\27\3\30\3\30\3\30\7\30\u011d\n\30\f\30\16")
        buf.write("\30\u0120\13\30\3\31\3\31\3\31\3\31\3\32\3\32\7\32\u0128")
        buf.write("\n\32\f\32\16\32\u012b\13\32\3\32\3\32\3\33\3\33\7\33")
        buf.write("\u0131\n\33\f\33\16\33\u0134\13\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0141\n\34\3")
        buf.write("\35\3\35\3\35\5\35\u0146\n\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u014d\n\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0162\n\"")
        buf.write("\5\"\u0164\n\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u0170")
        buf.write("\n$\3$\3$\3$\3$\3$\3$\5$\u0178\n$\3$\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\5\'\u0185\n\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\5)\u0190\n)\3)\3)\3)\3*\3*\3*\3*\3*\5*\u019a\n*\3")
        buf.write("+\3+\3+\3+\3+\5+\u01a1\n+\3,\3,\3,\3,\3,\3,\7,\u01a9\n")
        buf.write(",\f,\16,\u01ac\13,\3-\3-\3-\3-\3-\3-\7-\u01b4\n-\f-\16")
        buf.write("-\u01b7\13-\3.\3.\3.\3.\3.\3.\7.\u01bf\n.\f.\16.\u01c2")
        buf.write("\13.\3/\3/\3/\5/\u01c7\n/\3\60\3\60\3\60\5\60\u01cc\n")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u01d2\n\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u01dc\n\62\3\62\5\62\u01df")
        buf.write("\n\62\7\62\u01e1\n\62\f\62\16\62\u01e4\13\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u01eb\n\63\3\63\5\63\u01ee\n\63\3")
        buf.write("\63\5\63\u01f1\n\63\3\64\3\64\3\64\3\64\5\64\u01f7\n\64")
        buf.write("\3\64\3\64\5\64\u01fb\n\64\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\5\65\u0208\n\65\3\66\3\66")
        buf.write("\3\66\7\66\u020d\n\66\f\66\16\66\u0210\13\66\3\67\3\67")
        buf.write("\3\67\3\67\6\67\u0216\n\67\r\67\16\67\u0217\38\38\38\3")
        buf.write("8\38\38\38\58\u0221\n8\39\39\39\39\39\59\u0228\n9\39\3")
        buf.write("9\39\39\39\39\39\59\u0231\n9\39\59\u0234\n9\3:\3:\3:\3")
        buf.write(":\3:\5:\u023b\n:\3;\3;\3;\3;\3;\5;\u0242\n;\3<\3<\3<\3")
        buf.write("<\3<\7<\u0249\n<\f<\16<\u024c\13<\5<\u024e\n<\3<\3<\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\7>\u0259\n>\f>\16>\u025c\13>\5>\u025e")
        buf.write("\n>\3>\3>\3?\3?\3?\3?\3?\7?\u0267\n?\f?\16?\u026a\13?")
        buf.write("\5?\u026c\n?\3?\3?\3@\3@\3@\3@\3@\7@\u0275\n@\f@\16@\u0278")
        buf.write("\13@\5@\u027a\n@\3@\3@\3A\3A\3A\3A\3A\7A\u0283\nA\fA\16")
        buf.write("A\u0286\13A\5A\u0288\nA\3A\3A\3B\3B\5B\u028e\nB\3C\3C")
        buf.write("\3C\3C\3C\7C\u0295\nC\fC\16C\u0298\13C\5C\u029a\nC\3C")
        buf.write("\3C\3C\2\6VXZbD\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\u0082\u0084\2\n\3\2\24\25\3\2=>\3\2*+\4\2")
        buf.write("##%)\3\2!\"\3\2\33\34\3\2\35\37\3\2;<\2\u02b9\2\u0087")
        buf.write("\3\2\2\2\4\u008d\3\2\2\2\6\u008f\3\2\2\2\b\u0097\3\2\2")
        buf.write("\2\n\u00a4\3\2\2\2\f\u00a6\3\2\2\2\16\u00ab\3\2\2\2\20")
        buf.write("\u00b3\3\2\2\2\22\u00bb\3\2\2\2\24\u00c0\3\2\2\2\26\u00c5")
        buf.write("\3\2\2\2\30\u00d4\3\2\2\2\32\u00d6\3\2\2\2\34\u00d8\3")
        buf.write("\2\2\2\36\u00e0\3\2\2\2 \u00e2\3\2\2\2\"\u00ea\3\2\2\2")
        buf.write("$\u00ef\3\2\2\2&\u00fe\3\2\2\2(\u0106\3\2\2\2*\u010d\3")
        buf.write("\2\2\2,\u010f\3\2\2\2.\u0119\3\2\2\2\60\u0121\3\2\2\2")
        buf.write("\62\u0125\3\2\2\2\64\u012e\3\2\2\2\66\u0140\3\2\2\28\u0142")
        buf.write("\3\2\2\2:\u014c\3\2\2\2<\u0152\3\2\2\2>\u0156\3\2\2\2")
        buf.write("@\u0159\3\2\2\2B\u0163\3\2\2\2D\u0165\3\2\2\2F\u0168\3")
        buf.write("\2\2\2H\u017c\3\2\2\2J\u017f\3\2\2\2L\u0182\3\2\2\2N\u0188")
        buf.write("\3\2\2\2P\u018b\3\2\2\2R\u0199\3\2\2\2T\u01a0\3\2\2\2")
        buf.write("V\u01a2\3\2\2\2X\u01ad\3\2\2\2Z\u01b8\3\2\2\2\\\u01c6")
        buf.write("\3\2\2\2^\u01cb\3\2\2\2`\u01d1\3\2\2\2b\u01d3\3\2\2\2")
        buf.write("d\u01f0\3\2\2\2f\u01fa\3\2\2\2h\u0207\3\2\2\2j\u0209\3")
        buf.write("\2\2\2l\u0215\3\2\2\2n\u0220\3\2\2\2p\u0233\3\2\2\2r\u023a")
        buf.write("\3\2\2\2t\u0241\3\2\2\2v\u0243\3\2\2\2x\u0251\3\2\2\2")
        buf.write("z\u0253\3\2\2\2|\u0261\3\2\2\2~\u026f\3\2\2\2\u0080\u027d")
        buf.write("\3\2\2\2\u0082\u028d\3\2\2\2\u0084\u028f\3\2\2\2\u0086")
        buf.write("\u0088\5\4\3\2\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3")
        buf.write("\2\2\2\u008b\u008c\7\2\2\3\u008c\3\3\2\2\2\u008d\u008e")
        buf.write("\5\6\4\2\u008e\5\3\2\2\2\u008f\u0090\7\23\2\2\u0090\u0093")
        buf.write("\7>\2\2\u0091\u0092\7\66\2\2\u0092\u0094\7>\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u0096\5\b\5\2\u0096\7\3\2\2\2\u0097\u009b\7\60")
        buf.write("\2\2\u0098\u009a\5\n\6\2\u0099\u0098\3\2\2\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7\61\2")
        buf.write("\2\u009f\t\3\2\2\2\u00a0\u00a5\5\f\7\2\u00a1\u00a5\5\16")
        buf.write("\b\2\u00a2\u00a5\5\20\t\2\u00a3\u00a5\5\22\n\2\u00a4\u00a0")
        buf.write("\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\13\3\2\2\2\u00a6\u00a9\t\2\2\2\u00a7")
        buf.write("\u00aa\5\24\13\2\u00a8\u00aa\5\26\f\2\u00a9\u00a7\3\2")
        buf.write("\2\2\u00a9\u00a8\3\2\2\2\u00aa\r\3\2\2\2\u00ab\u00ac\t")
        buf.write("\3\2\2\u00ac\u00ae\7.\2\2\u00ad\u00af\5.\30\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00b1\7/\2\2\u00b1\u00b2\5\62\32\2\u00b2\17\3\2\2\2\u00b3")
        buf.write("\u00b4\7\27\2\2\u00b4\u00b6\7.\2\2\u00b5\u00b7\5.\30\2")
        buf.write("\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00b9\7/\2\2\u00b9\u00ba\5\62\32\2\u00ba")
        buf.write("\21\3\2\2\2\u00bb\u00bc\7\30\2\2\u00bc\u00bd\7.\2\2\u00bd")
        buf.write("\u00be\7/\2\2\u00be\u00bf\5\62\32\2\u00bf\23\3\2\2\2\u00c0")
        buf.write("\u00c1\5\34\17\2\u00c1\u00c2\7\66\2\2\u00c2\u00c3\5(\25")
        buf.write("\2\u00c3\u00c4\7\62\2\2\u00c4\25\3\2\2\2\u00c5\u00c6\5")
        buf.write("\32\16\2\u00c6\u00c7\5\30\r\2\u00c7\u00c8\5R*\2\u00c8")
        buf.write("\u00c9\7\62\2\2\u00c9\27\3\2\2\2\u00ca\u00cb\7\63\2\2")
        buf.write("\u00cb\u00cc\5\32\16\2\u00cc\u00cd\5\30\r\2\u00cd\u00ce")
        buf.write("\5R*\2\u00ce\u00cf\7\63\2\2\u00cf\u00d5\3\2\2\2\u00d0")
        buf.write("\u00d1\7\66\2\2\u00d1\u00d2\5(\25\2\u00d2\u00d3\7$\2\2")
        buf.write("\u00d3\u00d5\3\2\2\2\u00d4\u00ca\3\2\2\2\u00d4\u00d0\3")
        buf.write("\2\2\2\u00d5\31\3\2\2\2\u00d6\u00d7\t\3\2\2\u00d7\33\3")
        buf.write("\2\2\2\u00d8\u00dd\5\32\16\2\u00d9\u00da\7\63\2\2\u00da")
        buf.write("\u00dc\5\32\16\2\u00db\u00d9\3\2\2\2\u00dc\u00df\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\35\3")
        buf.write("\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1\37")
        buf.write("\3\2\2\2\u00e2\u00e7\5\36\20\2\u00e3\u00e4\7\63\2\2\u00e4")
        buf.write("\u00e6\5\36\20\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2")
        buf.write("\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8!\3\2")
        buf.write("\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\5 \21\2\u00eb\u00ec")
        buf.write("\7\66\2\2\u00ec\u00ed\5(\25\2\u00ed\u00ee\7\62\2\2\u00ee")
        buf.write("#\3\2\2\2\u00ef\u00f0\5\36\20\2\u00f0\u00f1\5&\24\2\u00f1")
        buf.write("\u00f2\5R*\2\u00f2\u00f3\7\62\2\2\u00f3%\3\2\2\2\u00f4")
        buf.write("\u00f5\7\63\2\2\u00f5\u00f6\5\36\20\2\u00f6\u00f7\5&\24")
        buf.write("\2\u00f7\u00f8\5R*\2\u00f8\u00f9\7\63\2\2\u00f9\u00ff")
        buf.write("\3\2\2\2\u00fa\u00fb\7\66\2\2\u00fb\u00fc\5(\25\2\u00fc")
        buf.write("\u00fd\7$\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00f4\3\2\2\2")
        buf.write("\u00fe\u00fa\3\2\2\2\u00ff\'\3\2\2\2\u0100\u0107\7\17")
        buf.write("\2\2\u0101\u0107\7\r\2\2\u0102\u0107\7\16\2\2\u0103\u0107")
        buf.write("\7\20\2\2\u0104\u0107\5,\27\2\u0105\u0107\7>\2\2\u0106")
        buf.write("\u0100\3\2\2\2\u0106\u0101\3\2\2\2\u0106\u0102\3\2\2\2")
        buf.write("\u0106\u0103\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0105\3")
        buf.write("\2\2\2\u0107)\3\2\2\2\u0108\u010e\7\17\2\2\u0109\u010e")
        buf.write("\7\r\2\2\u010a\u010e\7\16\2\2\u010b\u010e\7\20\2\2\u010c")
        buf.write("\u010e\5,\27\2\u010d\u0108\3\2\2\2\u010d\u0109\3\2\2\2")
        buf.write("\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c\3")
        buf.write("\2\2\2\u010e+\3\2\2\2\u010f\u0110\7\13\2\2\u0110\u0115")
        buf.write("\7\64\2\2\u0111\u0112\5*\26\2\u0112\u0113\7\63\2\2\u0113")
        buf.write("\u0114\7;\2\2\u0114\u0116\3\2\2\2\u0115\u0111\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7")
        buf.write("\65\2\2\u0118-\3\2\2\2\u0119\u011e\5\60\31\2\u011a\u011b")
        buf.write("\7\62\2\2\u011b\u011d\5\60\31\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f/\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\5 \21")
        buf.write("\2\u0122\u0123\7\66\2\2\u0123\u0124\5(\25\2\u0124\61\3")
        buf.write("\2\2\2\u0125\u0129\7\60\2\2\u0126\u0128\5\66\34\2\u0127")
        buf.write("\u0126\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0129\3")
        buf.write("\2\2\2\u012c\u012d\7\61\2\2\u012d\63\3\2\2\2\u012e\u0132")
        buf.write("\7\60\2\2\u012f\u0131\5\66\34\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\7")
        buf.write("\61\2\2\u0136\65\3\2\2\2\u0137\u0141\5:\36\2\u0138\u0141")
        buf.write("\5<\37\2\u0139\u0141\5J&\2\u013a\u0141\5H%\2\u013b\u0141")
        buf.write("\5F$\2\u013c\u0141\5L\'\2\u013d\u0141\5N(\2\u013e\u0141")
        buf.write("\5\64\33\2\u013f\u0141\58\35\2\u0140\u0137\3\2\2\2\u0140")
        buf.write("\u0138\3\2\2\2\u0140\u0139\3\2\2\2\u0140\u013a\3\2\2\2")
        buf.write("\u0140\u013b\3\2\2\2\u0140\u013c\3\2\2\2\u0140\u013d\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141\67")
        buf.write("\3\2\2\2\u0142\u0145\t\2\2\2\u0143\u0146\5\"\22\2\u0144")
        buf.write("\u0146\5$\23\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u01469\3\2\2\2\u0147\u0148\5b\62\2\u0148\u0149\5l\67")
        buf.write("\2\u0149\u014d\3\2\2\2\u014a\u014d\7>\2\2\u014b\u014d")
        buf.write("\5n8\2\u014c\u0147\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\7$\2\2\u014f")
        buf.write("\u0150\5R*\2\u0150\u0151\7\62\2\2\u0151;\3\2\2\2\u0152")
        buf.write("\u0153\7\5\2\2\u0153\u0154\5> \2\u0154\u0155\5B\"\2\u0155")
        buf.write("=\3\2\2\2\u0156\u0157\5R*\2\u0157\u0158\5\62\32\2\u0158")
        buf.write("?\3\2\2\2\u0159\u015a\7\6\2\2\u015a\u015b\5R*\2\u015b")
        buf.write("\u015c\5\62\32\2\u015cA\3\2\2\2\u015d\u015e\5@!\2\u015e")
        buf.write("\u015f\5B\"\2\u015f\u0164\3\2\2\2\u0160\u0162\5D#\2\u0161")
        buf.write("\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\3\2\2\2")
        buf.write("\u0163\u015d\3\2\2\2\u0163\u0161\3\2\2\2\u0164C\3\2\2")
        buf.write("\2\u0165\u0166\7\7\2\2\u0166\u0167\5\62\32\2\u0167E\3")
        buf.write("\2\2\2\u0168\u0169\7\b\2\2\u0169\u016f\7.\2\2\u016a\u016b")
        buf.write("\5b\62\2\u016b\u016c\5l\67\2\u016c\u0170\3\2\2\2\u016d")
        buf.write("\u0170\7>\2\2\u016e\u0170\5n8\2\u016f\u016a\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0172\7\f\2\2\u0172\u0173\5R*\2\u0173\u0174\7\67")
        buf.write("\2\2\u0174\u0177\5R*\2\u0175\u0176\7\31\2\2\u0176\u0178")
        buf.write("\5R*\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017a\7/\2\2\u017a\u017b\5\62\32\2\u017b")
        buf.write("G\3\2\2\2\u017c\u017d\7\3\2\2\u017d\u017e\7\62\2\2\u017e")
        buf.write("I\3\2\2\2\u017f\u0180\7\4\2\2\u0180\u0181\7\62\2\2\u0181")
        buf.write("K\3\2\2\2\u0182\u0184\7\21\2\2\u0183\u0185\5R*\2\u0184")
        buf.write("\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0187\7\62\2\2\u0187M\3\2\2\2\u0188\u0189\5p9\2")
        buf.write("\u0189\u018a\7\62\2\2\u018aO\3\2\2\2\u018b\u018c\7\32")
        buf.write("\2\2\u018c\u018d\7>\2\2\u018d\u018f\7.\2\2\u018e\u0190")
        buf.write("\5j\66\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\7/\2\2\u0192\u0193\7\62\2\2")
        buf.write("\u0193Q\3\2\2\2\u0194\u0195\5T+\2\u0195\u0196\t\4\2\2")
        buf.write("\u0196\u0197\5T+\2\u0197\u019a\3\2\2\2\u0198\u019a\5T")
        buf.write("+\2\u0199\u0194\3\2\2\2\u0199\u0198\3\2\2\2\u019aS\3\2")
        buf.write("\2\2\u019b\u019c\5V,\2\u019c\u019d\t\5\2\2\u019d\u019e")
        buf.write("\5V,\2\u019e\u01a1\3\2\2\2\u019f\u01a1\5V,\2\u01a0\u019b")
        buf.write("\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1U\3\2\2\2\u01a2\u01a3")
        buf.write("\b,\1\2\u01a3\u01a4\5X-\2\u01a4\u01aa\3\2\2\2\u01a5\u01a6")
        buf.write("\f\4\2\2\u01a6\u01a7\t\6\2\2\u01a7\u01a9\5X-\2\u01a8\u01a5")
        buf.write("\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01abW\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad")
        buf.write("\u01ae\b-\1\2\u01ae\u01af\5Z.\2\u01af\u01b5\3\2\2\2\u01b0")
        buf.write("\u01b1\f\4\2\2\u01b1\u01b2\t\7\2\2\u01b2\u01b4\5Z.\2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6Y\3\2\2\2\u01b7\u01b5\3\2\2")
        buf.write("\2\u01b8\u01b9\b.\1\2\u01b9\u01ba\5\\/\2\u01ba\u01c0\3")
        buf.write("\2\2\2\u01bb\u01bc\f\4\2\2\u01bc\u01bd\t\b\2\2\u01bd\u01bf")
        buf.write("\5\\/\2\u01be\u01bb\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1[\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c4\7 \2\2\u01c4\u01c7\5\\/\2\u01c5")
        buf.write("\u01c7\5^\60\2\u01c6\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7]\3\2\2\2\u01c8\u01c9\7\34\2\2\u01c9\u01cc\5^\60")
        buf.write("\2\u01ca\u01cc\5`\61\2\u01cb\u01c8\3\2\2\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cc_\3\2\2\2\u01cd\u01ce\5b\62\2\u01ce\u01cf")
        buf.write("\5l\67\2\u01cf\u01d2\3\2\2\2\u01d0\u01d2\5b\62\2\u01d1")
        buf.write("\u01cd\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2a\3\2\2\2\u01d3")
        buf.write("\u01d4\b\62\1\2\u01d4\u01d5\5d\63\2\u01d5\u01e2\3\2\2")
        buf.write("\2\u01d6\u01d7\f\4\2\2\u01d7\u01d8\7-\2\2\u01d8\u01de")
        buf.write("\7>\2\2\u01d9\u01db\7.\2\2\u01da\u01dc\5j\66\2\u01db\u01da")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01df\7/\2\2\u01de\u01d9\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e1\3\2\2\2\u01e0\u01d6\3\2\2\2\u01e1\u01e4\3")
        buf.write("\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3c")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6")
        buf.write("\u01e7\7,\2\2\u01e7\u01ed\7=\2\2\u01e8\u01ea\7.\2\2\u01e9")
        buf.write("\u01eb\5j\66\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01ec\3\2\2\2\u01ec\u01ee\7/\2\2\u01ed\u01e8\3")
        buf.write("\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1")
        buf.write("\5f\64\2\u01f0\u01e5\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1")
        buf.write("e\3\2\2\2\u01f2\u01f3\7\32\2\2\u01f3\u01f4\7>\2\2\u01f4")
        buf.write("\u01f6\7.\2\2\u01f5\u01f7\5j\66\2\u01f6\u01f5\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fb\7")
        buf.write("/\2\2\u01f9\u01fb\5h\65\2\u01fa\u01f2\3\2\2\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fbg\3\2\2\2\u01fc\u0208\7>\2\2\u01fd\u0208")
        buf.write("\7\26\2\2\u01fe\u0208\5r:\2\u01ff\u0208\7;\2\2\u0200\u0201")
        buf.write("\7.\2\2\u0201\u0202\5R*\2\u0202\u0203\7/\2\2\u0203\u0208")
        buf.write("\3\2\2\2\u0204\u0208\7\t\2\2\u0205\u0208\7\n\2\2\u0206")
        buf.write("\u0208\7\22\2\2\u0207\u01fc\3\2\2\2\u0207\u01fd\3\2\2")
        buf.write("\2\u0207\u01fe\3\2\2\2\u0207\u01ff\3\2\2\2\u0207\u0200")
        buf.write("\3\2\2\2\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208i\3\2\2\2\u0209\u020e\5R*\2\u020a")
        buf.write("\u020b\7\63\2\2\u020b\u020d\5R*\2\u020c\u020a\3\2\2\2")
        buf.write("\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3")
        buf.write("\2\2\2\u020fk\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0212")
        buf.write("\7\64\2\2\u0212\u0213\5R*\2\u0213\u0214\7\65\2\2\u0214")
        buf.write("\u0216\3\2\2\2\u0215\u0211\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218m\3\2\2")
        buf.write("\2\u0219\u021a\5b\62\2\u021a\u021b\7-\2\2\u021b\u021c")
        buf.write("\7>\2\2\u021c\u0221\3\2\2\2\u021d\u021e\7>\2\2\u021e\u021f")
        buf.write("\7,\2\2\u021f\u0221\7=\2\2\u0220\u0219\3\2\2\2\u0220\u021d")
        buf.write("\3\2\2\2\u0221o\3\2\2\2\u0222\u0223\5b\62\2\u0223\u0224")
        buf.write("\7-\2\2\u0224\u0225\7>\2\2\u0225\u0227\7.\2\2\u0226\u0228")
        buf.write("\5j\66\2\u0227\u0226\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022a\7/\2\2\u022a\u0234\3\2\2\2")
        buf.write("\u022b\u022c\7>\2\2\u022c\u022d\7,\2\2\u022d\u022e\7=")
        buf.write("\2\2\u022e\u0230\7.\2\2\u022f\u0231\5j\66\2\u0230\u022f")
        buf.write("\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write("\u0234\7/\2\2\u0233\u0222\3\2\2\2\u0233\u022b\3\2\2\2")
        buf.write("\u0234q\3\2\2\2\u0235\u023b\7<\2\2\u0236\u023b\78\2\2")
        buf.write("\u0237\u023b\7:\2\2\u0238\u023b\79\2\2\u0239\u023b\5\u0082")
        buf.write("B\2\u023a\u0235\3\2\2\2\u023a\u0236\3\2\2\2\u023a\u0237")
        buf.write("\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u0239\3\2\2\2\u023b")
        buf.write("s\3\2\2\2\u023c\u0242\5z>\2\u023d\u0242\5|?\2\u023e\u0242")
        buf.write("\5~@\2\u023f\u0242\5\u0080A\2\u0240\u0242\5v<\2\u0241")
        buf.write("\u023c\3\2\2\2\u0241\u023d\3\2\2\2\u0241\u023e\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0241\u0240\3\2\2\2\u0242u\3\2\2")
        buf.write("\2\u0243\u0244\7\13\2\2\u0244\u024d\7.\2\2\u0245\u024a")
        buf.write("\5R*\2\u0246\u0247\7\63\2\2\u0247\u0249\5R*\2\u0248\u0246")
        buf.write("\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024a\3\2\2\2")
        buf.write("\u024d\u0245\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f\3")
        buf.write("\2\2\2\u024f\u0250\7/\2\2\u0250w\3\2\2\2\u0251\u0252\t")
        buf.write("\t\2\2\u0252y\3\2\2\2\u0253\u0254\7\13\2\2\u0254\u025d")
        buf.write("\7.\2\2\u0255\u025a\5x=\2\u0256\u0257\7\63\2\2\u0257\u0259")
        buf.write("\5x=\2\u0258\u0256\3\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025e\3\2\2\2\u025c")
        buf.write("\u025a\3\2\2\2\u025d\u0255\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u0260\7/\2\2\u0260{\3\2\2\2")
        buf.write("\u0261\u0262\7\13\2\2\u0262\u026b\7.\2\2\u0263\u0268\7")
        buf.write(":\2\2\u0264\u0265\7\63\2\2\u0265\u0267\7:\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0268")
        buf.write("\u0269\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268\3\2\2\2")
        buf.write("\u026b\u0263\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026d\3")
        buf.write("\2\2\2\u026d\u026e\7/\2\2\u026e}\3\2\2\2\u026f\u0270\7")
        buf.write("\13\2\2\u0270\u0279\7.\2\2\u0271\u0276\79\2\2\u0272\u0273")
        buf.write("\7\63\2\2\u0273\u0275\79\2\2\u0274\u0272\3\2\2\2\u0275")
        buf.write("\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u027a\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u0271\3")
        buf.write("\2\2\2\u0279\u027a\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u027c")
        buf.write("\7/\2\2\u027c\177\3\2\2\2\u027d\u027e\7\13\2\2\u027e\u0287")
        buf.write("\7.\2\2\u027f\u0284\78\2\2\u0280\u0281\7\63\2\2\u0281")
        buf.write("\u0283\78\2\2\u0282\u0280\3\2\2\2\u0283\u0286\3\2\2\2")
        buf.write("\u0284\u0282\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0288\3")
        buf.write("\2\2\2\u0286\u0284\3\2\2\2\u0287\u027f\3\2\2\2\u0287\u0288")
        buf.write("\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\7/\2\2\u028a")
        buf.write("\u0081\3\2\2\2\u028b\u028e\5t;\2\u028c\u028e\5\u0084C")
        buf.write("\2\u028d\u028b\3\2\2\2\u028d\u028c\3\2\2\2\u028e\u0083")
        buf.write("\3\2\2\2\u028f\u0290\7\13\2\2\u0290\u0299\7.\2\2\u0291")
        buf.write("\u0296\5\u0082B\2\u0292\u0293\7\63\2\2\u0293\u0295\5\u0082")
        buf.write("B\2\u0294\u0292\3\2\2\2\u0295\u0298\3\2\2\2\u0296\u0294")
        buf.write("\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u029a\3\2\2\2\u0298")
        buf.write("\u0296\3\2\2\2\u0299\u0291\3\2\2\2\u0299\u029a\3\2\2\2")
        buf.write("\u029a\u029b\3\2\2\2\u029b\u029c\7/\2\2\u029c\u0085\3")
        buf.write("\2\2\2B\u0089\u0093\u009b\u00a4\u00a9\u00ae\u00b6\u00d4")
        buf.write("\u00dd\u00e7\u00fe\u0106\u010d\u0115\u011e\u0129\u0132")
        buf.write("\u0140\u0145\u014c\u0161\u0163\u016f\u0177\u0184\u018f")
        buf.write("\u0199\u01a0\u01aa\u01b5\u01c0\u01c6\u01cb\u01d1\u01db")
        buf.write("\u01de\u01e2\u01ea\u01ed\u01f0\u01f6\u01fa\u0207\u020e")
        buf.write("\u0217\u0220\u0227\u0230\u0233\u023a\u0241\u024a\u024d")
        buf.write("\u025a\u025d\u0268\u026b\u0276\u0279\u0284\u0287\u028d")
        buf.write("\u0296\u0299")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Var'", "'Val'", 
                     "'Self'", "'Constructor'", "'Destructor'", "'By'", 
                     "'New'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'==.'", "'+.'", "'::'", "'.'", "'('", 
                     "')'", "'{'", "'}'", "';'", "','", "'['", "']'", "':'", 
                     "'..'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "KARRAY", "IN", 
                      "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "RETURN", 
                      "NULL", "CLASS", "VAR", "VAL", "SELF", "CONSTRUCTOR", 
                      "DESTRUCTOR", "BY", "NEW", "ADD_", "MINUS_", "MUL_", 
                      "DIV_", "MOD_", "EXCLAMATION_", "AND_", "OR_", "EQ_COMPARE", 
                      "EQ", "NOT_EQ_COMPARE", "SMALLER", "SM_OR_EQ", "GREATER", 
                      "GR_OR_EQ", "EQ_STRING", "ADD_STRING", "COLONCOLON", 
                      "DOT", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "LEFTB", 
                      "RIGHTB", "COLON", "DOTDOT", "BOOLEAN", "STRING", 
                      "FLOAT", "INT2", "INT", "DOLLAR_ID", "ID", "WS", "CMT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_type = 2
    RULE_class_block = 3
    RULE_class_stmt = 4
    RULE_attr_decl = 5
    RULE_method_decl = 6
    RULE_constructor = 7
    RULE_destructor = 8
    RULE_attr_decl_1 = 9
    RULE_attr_decl_2 = 10
    RULE_extend_1 = 11
    RULE_id_type = 12
    RULE_idList = 13
    RULE_nor_id_type = 14
    RULE_nor_idList = 15
    RULE_vari_decl_1 = 16
    RULE_vari_decl_2 = 17
    RULE_extend_2 = 18
    RULE_typeDeclaration = 19
    RULE_typeDeclaration2 = 20
    RULE_array_type = 21
    RULE_list_param = 22
    RULE_param_decl = 23
    RULE_stmt_block = 24
    RULE_stmt_block_ret = 25
    RULE_stmt = 26
    RULE_vari_decl = 27
    RULE_assign_stmt = 28
    RULE_if_stmt = 29
    RULE_condition_block = 30
    RULE_elseif_block = 31
    RULE_elseif_blocks = 32
    RULE_else_block = 33
    RULE_for_each_stmt = 34
    RULE_break_stmt = 35
    RULE_continue_stmt = 36
    RULE_return_stmt = 37
    RULE_method_inv_stmt = 38
    RULE_new_stmt = 39
    RULE_expr = 40
    RULE_expr1 = 41
    RULE_expr2 = 42
    RULE_expr3 = 43
    RULE_expr4 = 44
    RULE_expr5 = 45
    RULE_expr6 = 46
    RULE_expr7 = 47
    RULE_expr8 = 48
    RULE_expr9 = 49
    RULE_expr10 = 50
    RULE_primary = 51
    RULE_list_expr = 52
    RULE_index_op = 53
    RULE_member_access_attribute = 54
    RULE_member_access_method = 55
    RULE_literal = 56
    RULE_farray = 57
    RULE_expr_array = 58
    RULE_int_int2 = 59
    RULE_int_array = 60
    RULE_float_array = 61
    RULE_string_array = 62
    RULE_boolean_array = 63
    RULE_iarray = 64
    RULE_marray = 65

    ruleNames =  [ "program", "class_decl", "class_type", "class_block", 
                   "class_stmt", "attr_decl", "method_decl", "constructor", 
                   "destructor", "attr_decl_1", "attr_decl_2", "extend_1", 
                   "id_type", "idList", "nor_id_type", "nor_idList", "vari_decl_1", 
                   "vari_decl_2", "extend_2", "typeDeclaration", "typeDeclaration2", 
                   "array_type", "list_param", "param_decl", "stmt_block", 
                   "stmt_block_ret", "stmt", "vari_decl", "assign_stmt", 
                   "if_stmt", "condition_block", "elseif_block", "elseif_blocks", 
                   "else_block", "for_each_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_inv_stmt", "new_stmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "primary", "list_expr", 
                   "index_op", "member_access_attribute", "member_access_method", 
                   "literal", "farray", "expr_array", "int_int2", "int_array", 
                   "float_array", "string_array", "boolean_array", "iarray", 
                   "marray" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    TRUE=7
    FALSE=8
    KARRAY=9
    IN=10
    K_INT=11
    K_FLOAT=12
    K_BOOLEAN=13
    K_STRING=14
    RETURN=15
    NULL=16
    CLASS=17
    VAR=18
    VAL=19
    SELF=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    BY=23
    NEW=24
    ADD_=25
    MINUS_=26
    MUL_=27
    DIV_=28
    MOD_=29
    EXCLAMATION_=30
    AND_=31
    OR_=32
    EQ_COMPARE=33
    EQ=34
    NOT_EQ_COMPARE=35
    SMALLER=36
    SM_OR_EQ=37
    GREATER=38
    GR_OR_EQ=39
    EQ_STRING=40
    ADD_STRING=41
    COLONCOLON=42
    DOT=43
    LB=44
    RB=45
    LP=46
    RP=47
    SEMI=48
    COMMA=49
    LEFTB=50
    RIGHTB=51
    COLON=52
    DOTDOT=53
    BOOLEAN=54
    STRING=55
    FLOAT=56
    INT2=57
    INT=58
    DOLLAR_ID=59
    ID=60
    WS=61
    CMT=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.class_decl()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 137
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.class_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def class_block(self):
            return self.getTypedRuleContext(D96Parser.Class_blockContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(D96Parser.CLASS)
            self.state = 142
            self.match(D96Parser.ID)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 143
                self.match(D96Parser.COLON)
                self.state = 144
                self.match(D96Parser.ID)


            self.state = 147
            self.class_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def class_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_stmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_block" ):
                return visitor.visitClass_block(self)
            else:
                return visitor.visitChildren(self)




    def class_block(self):

        localctx = D96Parser.Class_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.LP)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 150
                self.class_stmt()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_stmt" ):
                return visitor.visitClass_stmt(self)
            else:
                return visitor.visitChildren(self)




    def class_stmt(self):

        localctx = D96Parser.Class_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_stmt)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR, D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.attr_decl()
                pass
            elif token in [D96Parser.DOLLAR_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.method_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def attr_decl_1(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_1Context,0)


        def attr_decl_2(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 165
                self.attr_decl_1()
                pass

            elif la_ == 2:
                self.state = 166
                self.attr_decl_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
            self.match(D96Parser.LB)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 171
                self.list_param()


            self.state = 174
            self.match(D96Parser.RB)
            self.state = 175
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 178
            self.match(D96Parser.LB)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 179
                self.list_param()


            self.state = 182
            self.match(D96Parser.RB)
            self.state = 183
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(D96Parser.DESTRUCTOR)
            self.state = 186
            self.match(D96Parser.LB)
            self.state = 187
            self.match(D96Parser.RB)
            self.state = 188
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(D96Parser.IdListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclarationContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_1" ):
                return visitor.visitAttr_decl_1(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_1(self):

        localctx = D96Parser.Attr_decl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_decl_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.idList()
            self.state = 191
            self.match(D96Parser.COLON)
            self.state = 192
            self.typeDeclaration()
            self.state = 193
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(D96Parser.Id_typeContext,0)


        def extend_1(self):
            return self.getTypedRuleContext(D96Parser.Extend_1Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_2" ):
                return visitor.visitAttr_decl_2(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_2(self):

        localctx = D96Parser.Attr_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_decl_2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.id_type()
            self.state = 196
            self.extend_1()
            self.state = 197
            self.expr()
            self.state = 198
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extend_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def id_type(self):
            return self.getTypedRuleContext(D96Parser.Id_typeContext,0)


        def extend_1(self):
            return self.getTypedRuleContext(D96Parser.Extend_1Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclarationContext,0)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_extend_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtend_1" ):
                return visitor.visitExtend_1(self)
            else:
                return visitor.visitChildren(self)




    def extend_1(self):

        localctx = D96Parser.Extend_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_extend_1)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(D96Parser.COMMA)
                self.state = 201
                self.id_type()
                self.state = 202
                self.extend_1()
                self.state = 203
                self.expr()
                self.state = 204
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(D96Parser.COLON)
                self.state = 207
                self.typeDeclaration()
                self.state = 208
                self.match(D96Parser.EQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_id_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_type" ):
                return visitor.visitId_type(self)
            else:
                return visitor.visitChildren(self)




    def id_type(self):

        localctx = D96Parser.Id_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Id_typeContext)
            else:
                return self.getTypedRuleContext(D96Parser.Id_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = D96Parser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.id_type()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 215
                self.match(D96Parser.COMMA)
                self.state = 216
                self.id_type()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nor_id_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_nor_id_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNor_id_type" ):
                return visitor.visitNor_id_type(self)
            else:
                return visitor.visitChildren(self)




    def nor_id_type(self):

        localctx = D96Parser.Nor_id_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nor_id_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nor_idListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nor_id_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Nor_id_typeContext)
            else:
                return self.getTypedRuleContext(D96Parser.Nor_id_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_nor_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNor_idList" ):
                return visitor.visitNor_idList(self)
            else:
                return visitor.visitChildren(self)




    def nor_idList(self):

        localctx = D96Parser.Nor_idListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nor_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.nor_id_type()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 225
                self.match(D96Parser.COMMA)
                self.state = 226
                self.nor_id_type()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decl_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nor_idList(self):
            return self.getTypedRuleContext(D96Parser.Nor_idListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclarationContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_vari_decl_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decl_1" ):
                return visitor.visitVari_decl_1(self)
            else:
                return visitor.visitChildren(self)




    def vari_decl_1(self):

        localctx = D96Parser.Vari_decl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vari_decl_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.nor_idList()
            self.state = 233
            self.match(D96Parser.COLON)
            self.state = 234
            self.typeDeclaration()
            self.state = 235
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decl_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nor_id_type(self):
            return self.getTypedRuleContext(D96Parser.Nor_id_typeContext,0)


        def extend_2(self):
            return self.getTypedRuleContext(D96Parser.Extend_2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_vari_decl_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decl_2" ):
                return visitor.visitVari_decl_2(self)
            else:
                return visitor.visitChildren(self)




    def vari_decl_2(self):

        localctx = D96Parser.Vari_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vari_decl_2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.nor_id_type()
            self.state = 238
            self.extend_2()
            self.state = 239
            self.expr()
            self.state = 240
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extend_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def nor_id_type(self):
            return self.getTypedRuleContext(D96Parser.Nor_id_typeContext,0)


        def extend_2(self):
            return self.getTypedRuleContext(D96Parser.Extend_2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclarationContext,0)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_extend_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtend_2" ):
                return visitor.visitExtend_2(self)
            else:
                return visitor.visitChildren(self)




    def extend_2(self):

        localctx = D96Parser.Extend_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_extend_2)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(D96Parser.COMMA)
                self.state = 243
                self.nor_id_type()
                self.state = 244
                self.extend_2()
                self.state = 245
                self.expr()
                self.state = 246
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(D96Parser.COLON)
                self.state = 249
                self.typeDeclaration()
                self.state = 250
                self.match(D96Parser.EQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BOOLEAN(self):
            return self.getToken(D96Parser.K_BOOLEAN, 0)

        def K_INT(self):
            return self.getToken(D96Parser.K_INT, 0)

        def K_FLOAT(self):
            return self.getToken(D96Parser.K_FLOAT, 0)

        def K_STRING(self):
            return self.getToken(D96Parser.K_STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typeDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDeclaration" ):
                return visitor.visitTypeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typeDeclaration(self):

        localctx = D96Parser.TypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_BOOLEAN]:
                self.state = 254
                self.match(D96Parser.K_BOOLEAN)
                pass
            elif token in [D96Parser.K_INT]:
                self.state = 255
                self.match(D96Parser.K_INT)
                pass
            elif token in [D96Parser.K_FLOAT]:
                self.state = 256
                self.match(D96Parser.K_FLOAT)
                pass
            elif token in [D96Parser.K_STRING]:
                self.state = 257
                self.match(D96Parser.K_STRING)
                pass
            elif token in [D96Parser.KARRAY]:
                self.state = 258
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.state = 259
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclaration2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BOOLEAN(self):
            return self.getToken(D96Parser.K_BOOLEAN, 0)

        def K_INT(self):
            return self.getToken(D96Parser.K_INT, 0)

        def K_FLOAT(self):
            return self.getToken(D96Parser.K_FLOAT, 0)

        def K_STRING(self):
            return self.getToken(D96Parser.K_STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typeDeclaration2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDeclaration2" ):
                return visitor.visitTypeDeclaration2(self)
            else:
                return visitor.visitChildren(self)




    def typeDeclaration2(self):

        localctx = D96Parser.TypeDeclaration2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeDeclaration2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_BOOLEAN]:
                self.state = 262
                self.match(D96Parser.K_BOOLEAN)
                pass
            elif token in [D96Parser.K_INT]:
                self.state = 263
                self.match(D96Parser.K_INT)
                pass
            elif token in [D96Parser.K_FLOAT]:
                self.state = 264
                self.match(D96Parser.K_FLOAT)
                pass
            elif token in [D96Parser.K_STRING]:
                self.state = 265
                self.match(D96Parser.K_STRING)
                pass
            elif token in [D96Parser.KARRAY]:
                self.state = 266
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LEFTB(self):
            return self.getToken(D96Parser.LEFTB, 0)

        def RIGHTB(self):
            return self.getToken(D96Parser.RIGHTB, 0)

        def typeDeclaration2(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclaration2Context,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INT2(self):
            return self.getToken(D96Parser.INT2, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(D96Parser.KARRAY)
            self.state = 270
            self.match(D96Parser.LEFTB)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.KARRAY) | (1 << D96Parser.K_INT) | (1 << D96Parser.K_FLOAT) | (1 << D96Parser.K_BOOLEAN) | (1 << D96Parser.K_STRING))) != 0):
                self.state = 271
                self.typeDeclaration2()
                self.state = 272
                self.match(D96Parser.COMMA)
                self.state = 273
                self.match(D96Parser.INT2)


            self.state = 277
            self.match(D96Parser.RIGHTB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Param_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Param_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = D96Parser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.param_decl()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 280
                self.match(D96Parser.SEMI)
                self.state = 281
                self.param_decl()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nor_idList(self):
            return self.getTypedRuleContext(D96Parser.Nor_idListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = D96Parser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.nor_idList()
            self.state = 288
            self.match(D96Parser.COLON)
            self.state = 289
            self.typeDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = D96Parser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(D96Parser.LP)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                self.state = 292
                self.stmt()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_block_retContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_block_ret

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block_ret" ):
                return visitor.visitStmt_block_ret(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block_ret(self):

        localctx = D96Parser.Stmt_block_retContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_block_ret)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(D96Parser.LP)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                self.state = 301
                self.stmt()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def for_each_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_each_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_inv_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_inv_stmtContext,0)


        def stmt_block_ret(self):
            return self.getTypedRuleContext(D96Parser.Stmt_block_retContext,0)


        def vari_decl(self):
            return self.getTypedRuleContext(D96Parser.Vari_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.for_each_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 314
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 315
                self.method_inv_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 316
                self.stmt_block_ret()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 317
                self.vari_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def vari_decl_1(self):
            return self.getTypedRuleContext(D96Parser.Vari_decl_1Context,0)


        def vari_decl_2(self):
            return self.getTypedRuleContext(D96Parser.Vari_decl_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_vari_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decl" ):
                return visitor.visitVari_decl(self)
            else:
                return visitor.visitChildren(self)




    def vari_decl(self):

        localctx = D96Parser.Vari_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_vari_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 321
                self.vari_decl_1()
                pass

            elif la_ == 2:
                self.state = 322
                self.vari_decl_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def member_access_attribute(self):
            return self.getTypedRuleContext(D96Parser.Member_access_attributeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 325
                self.expr8(0)
                self.state = 326
                self.index_op()
                pass

            elif la_ == 2:
                self.state = 328
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 329
                self.member_access_attribute()
                pass


            self.state = 332
            self.match(D96Parser.EQ)
            self.state = 333
            self.expr()
            self.state = 334
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def condition_block(self):
            return self.getTypedRuleContext(D96Parser.Condition_blockContext,0)


        def elseif_blocks(self):
            return self.getTypedRuleContext(D96Parser.Elseif_blocksContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.IF)
            self.state = 337
            self.condition_block()
            self.state = 338
            self.elseif_blocks()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_condition_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_block" ):
                return visitor.visitCondition_block(self)
            else:
                return visitor.visitChildren(self)




    def condition_block(self):

        localctx = D96Parser.Condition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_condition_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.expr()
            self.state = 341
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_block" ):
                return visitor.visitElseif_block(self)
            else:
                return visitor.visitChildren(self)




    def elseif_block(self):

        localctx = D96Parser.Elseif_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_elseif_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(D96Parser.ELSEIF)
            self.state = 344
            self.expr()
            self.state = 345
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_blocksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_block(self):
            return self.getTypedRuleContext(D96Parser.Elseif_blockContext,0)


        def elseif_blocks(self):
            return self.getTypedRuleContext(D96Parser.Elseif_blocksContext,0)


        def else_block(self):
            return self.getTypedRuleContext(D96Parser.Else_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_blocks

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_blocks" ):
                return visitor.visitElseif_blocks(self)
            else:
                return visitor.visitChildren(self)




    def elseif_blocks(self):

        localctx = D96Parser.Elseif_blocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elseif_blocks)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.elseif_block()
                self.state = 348
                self.elseif_blocks()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.TRUE, D96Parser.FALSE, D96Parser.KARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAR, D96Parser.VAL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.LP, D96Parser.RP, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.FLOAT, D96Parser.INT2, D96Parser.INT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ELSE:
                    self.state = 350
                    self.else_block()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_block" ):
                return visitor.visitElse_block(self)
            else:
                return visitor.visitChildren(self)




    def else_block(self):

        localctx = D96Parser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(D96Parser.ELSE)
            self.state = 356
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_each_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def member_access_attribute(self):
            return self.getTypedRuleContext(D96Parser.Member_access_attributeContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_each_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each_stmt" ):
                return visitor.visitFor_each_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_each_stmt(self):

        localctx = D96Parser.For_each_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_each_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(D96Parser.FOREACH)
            self.state = 359
            self.match(D96Parser.LB)
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 360
                self.expr8(0)
                self.state = 361
                self.index_op()
                pass

            elif la_ == 2:
                self.state = 363
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 364
                self.member_access_attribute()
                pass


            self.state = 367
            self.match(D96Parser.IN)
            self.state = 368
            self.expr()
            self.state = 369
            self.match(D96Parser.DOTDOT)
            self.state = 370
            self.expr()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 371
                self.match(D96Parser.BY)
                self.state = 372
                self.expr()


            self.state = 375
            self.match(D96Parser.RB)
            self.state = 376
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.BREAK)
            self.state = 379
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(D96Parser.CONTINUE)
            self.state = 382
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(D96Parser.RETURN)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                self.state = 385
                self.expr()


            self.state = 388
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_inv_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_method(self):
            return self.getTypedRuleContext(D96Parser.Member_access_methodContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_inv_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_inv_stmt" ):
                return visitor.visitMethod_inv_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_inv_stmt(self):

        localctx = D96Parser.Method_inv_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_method_inv_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.member_access_method()
            self.state = 391
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_new_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_stmt" ):
                return visitor.visitNew_stmt(self)
            else:
                return visitor.visitChildren(self)




    def new_stmt(self):

        localctx = D96Parser.New_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_new_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(D96Parser.NEW)
            self.state = 394
            self.match(D96Parser.ID)
            self.state = 395
            self.match(D96Parser.LB)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                self.state = 396
                self.list_expr()


            self.state = 399
            self.match(D96Parser.RB)
            self.state = 400
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def ADD_STRING(self):
            return self.getToken(D96Parser.ADD_STRING, 0)

        def EQ_STRING(self):
            return self.getToken(D96Parser.EQ_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.expr1()
                self.state = 403
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQ_STRING or _la==D96Parser.ADD_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 404
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQ_COMPARE(self):
            return self.getToken(D96Parser.EQ_COMPARE, 0)

        def NOT_EQ_COMPARE(self):
            return self.getToken(D96Parser.NOT_EQ_COMPARE, 0)

        def SMALLER(self):
            return self.getToken(D96Parser.SMALLER, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def SM_OR_EQ(self):
            return self.getToken(D96Parser.SM_OR_EQ, 0)

        def GR_OR_EQ(self):
            return self.getToken(D96Parser.GR_OR_EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.expr2(0)
                self.state = 410
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ_COMPARE) | (1 << D96Parser.NOT_EQ_COMPARE) | (1 << D96Parser.SMALLER) | (1 << D96Parser.SM_OR_EQ) | (1 << D96Parser.GREATER) | (1 << D96Parser.GR_OR_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND_(self):
            return self.getToken(D96Parser.AND_, 0)

        def OR_(self):
            return self.getToken(D96Parser.OR_, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 419
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 420
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND_ or _la==D96Parser.OR_):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 421
                    self.expr3(0) 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD_(self):
            return self.getToken(D96Parser.ADD_, 0)

        def MINUS_(self):
            return self.getToken(D96Parser.MINUS_, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 430
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 431
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD_ or _la==D96Parser.MINUS_):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 432
                    self.expr4(0) 
                self.state = 437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MUL_(self):
            return self.getToken(D96Parser.MUL_, 0)

        def DIV_(self):
            return self.getToken(D96Parser.DIV_, 0)

        def MOD_(self):
            return self.getToken(D96Parser.MOD_, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 446
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 441
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 442
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL_) | (1 << D96Parser.DIV_) | (1 << D96Parser.MOD_))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 443
                    self.expr5() 
                self.state = 448
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATION_(self):
            return self.getToken(D96Parser.EXCLAMATION_, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr5)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EXCLAMATION_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(D96Parser.EXCLAMATION_)
                self.state = 450
                self.expr5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.KARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.MINUS_, D96Parser.LB, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.FLOAT, D96Parser.INT2, D96Parser.INT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS_(self):
            return self.getToken(D96Parser.MINUS_, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr6)
        try:
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(D96Parser.MINUS_)
                self.state = 455
                self.expr6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.KARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.FLOAT, D96Parser.INT2, D96Parser.INT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr7)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.expr8(0)
                self.state = 460
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 480
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 468
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 469
                    self.match(D96Parser.DOT)
                    self.state = 470
                    self.match(D96Parser.ID)
                    self.state = 476
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 471
                        self.match(D96Parser.LB)
                        self.state = 473
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                            self.state = 472
                            self.list_expr()


                        self.state = 475
                        self.match(D96Parser.RB)

             
                self.state = 482
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLONCOLON(self):
            return self.getToken(D96Parser.COLONCOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.match(D96Parser.ID)
                self.state = 484
                self.match(D96Parser.COLONCOLON)
                self.state = 485
                self.match(D96Parser.DOLLAR_ID)
                self.state = 491
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 486
                    self.match(D96Parser.LB)
                    self.state = 488
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                        self.state = 487
                        self.list_expr()


                    self.state = 490
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def primary(self):
            return self.getTypedRuleContext(D96Parser.PrimaryContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.match(D96Parser.NEW)
                self.state = 497
                self.match(D96Parser.ID)
                self.state = 498
                self.match(D96Parser.LB)
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                    self.state = 499
                    self.list_expr()


                self.state = 502
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.KARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.FLOAT, D96Parser.INT2, D96Parser.INT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def INT2(self):
            return self.getToken(D96Parser.INT2, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = D96Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_primary)
        try:
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.KARRAY, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.FLOAT, D96Parser.INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.literal()
                pass
            elif token in [D96Parser.INT2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 509
                self.match(D96Parser.INT2)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 510
                self.match(D96Parser.LB)
                self.state = 511
                self.expr()
                self.state = 512
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 514
                self.match(D96Parser.TRUE)
                pass
            elif token in [D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 515
                self.match(D96Parser.FALSE)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 516
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = D96Parser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_list_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.expr()
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 520
                self.match(D96Parser.COMMA)
                self.state = 521
                self.expr()
                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LEFTB)
            else:
                return self.getToken(D96Parser.LEFTB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RIGHTB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RIGHTB)
            else:
                return self.getToken(D96Parser.RIGHTB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = D96Parser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 527
                    self.match(D96Parser.LEFTB)
                    self.state = 528
                    self.expr()
                    self.state = 529
                    self.match(D96Parser.RIGHTB)

                else:
                    raise NoViableAltException(self)
                self.state = 533 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_access_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLONCOLON(self):
            return self.getToken(D96Parser.COLONCOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_access_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_attribute" ):
                return visitor.visitMember_access_attribute(self)
            else:
                return visitor.visitChildren(self)




    def member_access_attribute(self):

        localctx = D96Parser.Member_access_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_member_access_attribute)
        try:
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.expr8(0)
                self.state = 536
                self.match(D96Parser.DOT)
                self.state = 537
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.match(D96Parser.ID)
                self.state = 540
                self.match(D96Parser.COLONCOLON)
                self.state = 541
                self.match(D96Parser.DOLLAR_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_access_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def COLONCOLON(self):
            return self.getToken(D96Parser.COLONCOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_access_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_method" ):
                return visitor.visitMember_access_method(self)
            else:
                return visitor.visitChildren(self)




    def member_access_method(self):

        localctx = D96Parser.Member_access_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_member_access_method)
        self._la = 0 # Token type
        try:
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.expr8(0)
                self.state = 545
                self.match(D96Parser.DOT)
                self.state = 546
                self.match(D96Parser.ID)
                self.state = 547
                self.match(D96Parser.LB)
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                    self.state = 548
                    self.list_expr()


                self.state = 551
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.match(D96Parser.ID)
                self.state = 554
                self.match(D96Parser.COLONCOLON)
                self.state = 555
                self.match(D96Parser.DOLLAR_ID)
                self.state = 556
                self.match(D96Parser.LB)
                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                    self.state = 557
                    self.list_expr()


                self.state = 560
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def iarray(self):
            return self.getTypedRuleContext(D96Parser.IarrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_literal)
        try:
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 565
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 566
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.KARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 567
                self.iarray()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_array(self):
            return self.getTypedRuleContext(D96Parser.Int_arrayContext,0)


        def float_array(self):
            return self.getTypedRuleContext(D96Parser.Float_arrayContext,0)


        def string_array(self):
            return self.getTypedRuleContext(D96Parser.String_arrayContext,0)


        def boolean_array(self):
            return self.getTypedRuleContext(D96Parser.Boolean_arrayContext,0)


        def expr_array(self):
            return self.getTypedRuleContext(D96Parser.Expr_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_farray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFarray" ):
                return visitor.visitFarray(self)
            else:
                return visitor.visitChildren(self)




    def farray(self):

        localctx = D96Parser.FarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_farray)
        try:
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.int_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 571
                self.float_array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 572
                self.string_array()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 573
                self.boolean_array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 574
                self.expr_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_array" ):
                return visitor.visitExpr_array(self)
            else:
                return visitor.visitChildren(self)




    def expr_array(self):

        localctx = D96Parser.Expr_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(D96Parser.KARRAY)
            self.state = 578
            self.match(D96Parser.LB)
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.KARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.MINUS_) | (1 << D96Parser.EXCLAMATION_) | (1 << D96Parser.LB) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT2) | (1 << D96Parser.INT) | (1 << D96Parser.ID))) != 0):
                self.state = 579
                self.expr()
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 580
                    self.match(D96Parser.COMMA)
                    self.state = 581
                    self.expr()
                    self.state = 586
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 589
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_int2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def INT2(self):
            return self.getToken(D96Parser.INT2, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_int_int2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_int2" ):
                return visitor.visitInt_int2(self)
            else:
                return visitor.visitChildren(self)




    def int_int2(self):

        localctx = D96Parser.Int_int2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_int_int2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            _la = self._input.LA(1)
            if not(_la==D96Parser.INT2 or _la==D96Parser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def int_int2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Int_int2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Int_int2Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_int_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_array" ):
                return visitor.visitInt_array(self)
            else:
                return visitor.visitChildren(self)




    def int_array(self):

        localctx = D96Parser.Int_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_int_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(D96Parser.KARRAY)
            self.state = 594
            self.match(D96Parser.LB)
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INT2 or _la==D96Parser.INT:
                self.state = 595
                self.int_int2()
                self.state = 600
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 596
                    self.match(D96Parser.COMMA)
                    self.state = 597
                    self.int_int2()
                    self.state = 602
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 605
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.FLOAT)
            else:
                return self.getToken(D96Parser.FLOAT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_float_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_array" ):
                return visitor.visitFloat_array(self)
            else:
                return visitor.visitChildren(self)




    def float_array(self):

        localctx = D96Parser.Float_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_float_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(D96Parser.KARRAY)
            self.state = 608
            self.match(D96Parser.LB)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.FLOAT:
                self.state = 609
                self.match(D96Parser.FLOAT)
                self.state = 614
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 610
                    self.match(D96Parser.COMMA)
                    self.state = 611
                    self.match(D96Parser.FLOAT)
                    self.state = 616
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 619
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STRING)
            else:
                return self.getToken(D96Parser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_string_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_array" ):
                return visitor.visitString_array(self)
            else:
                return visitor.visitChildren(self)




    def string_array(self):

        localctx = D96Parser.String_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_string_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(D96Parser.KARRAY)
            self.state = 622
            self.match(D96Parser.LB)
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STRING:
                self.state = 623
                self.match(D96Parser.STRING)
                self.state = 628
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 624
                    self.match(D96Parser.COMMA)
                    self.state = 625
                    self.match(D96Parser.STRING)
                    self.state = 630
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 633
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.BOOLEAN)
            else:
                return self.getToken(D96Parser.BOOLEAN, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_boolean_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_array" ):
                return visitor.visitBoolean_array(self)
            else:
                return visitor.visitChildren(self)




    def boolean_array(self):

        localctx = D96Parser.Boolean_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_boolean_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(D96Parser.KARRAY)
            self.state = 636
            self.match(D96Parser.LB)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BOOLEAN:
                self.state = 637
                self.match(D96Parser.BOOLEAN)
                self.state = 642
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 638
                    self.match(D96Parser.COMMA)
                    self.state = 639
                    self.match(D96Parser.BOOLEAN)
                    self.state = 644
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 647
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def farray(self):
            return self.getTypedRuleContext(D96Parser.FarrayContext,0)


        def marray(self):
            return self.getTypedRuleContext(D96Parser.MarrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_iarray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIarray" ):
                return visitor.visitIarray(self)
            else:
                return visitor.visitChildren(self)




    def iarray(self):

        localctx = D96Parser.IarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_iarray)
        try:
            self.state = 651
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 649
                self.farray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 650
                self.marray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KARRAY(self):
            return self.getToken(D96Parser.KARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def iarray(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IarrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IarrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_marray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMarray" ):
                return visitor.visitMarray(self)
            else:
                return visitor.visitChildren(self)




    def marray(self):

        localctx = D96Parser.MarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_marray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(D96Parser.KARRAY)
            self.state = 654
            self.match(D96Parser.LB)
            self.state = 663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.KARRAY:
                self.state = 655
                self.iarray()
                self.state = 660
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 656
                    self.match(D96Parser.COMMA)
                    self.state = 657
                    self.iarray()
                    self.state = 662
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 665
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[42] = self.expr2_sempred
        self._predicates[43] = self.expr3_sempred
        self._predicates[44] = self.expr4_sempred
        self._predicates[48] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




