# Generated from baby_duck_grammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,222,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,5,0,53,8,0,10,
        0,12,0,56,9,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,1,0,1,0,1,0,1,0,1,
        1,1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,
        2,82,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,95,8,5,
        1,6,1,6,1,7,1,7,1,8,1,8,1,8,5,8,104,8,8,10,8,12,8,107,9,8,1,9,1,
        9,1,9,5,9,112,8,9,10,9,12,9,115,9,9,3,9,117,8,9,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,130,8,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,5,12,140,8,12,10,12,12,12,143,9,12,1,
        12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,4,13,153,8,13,11,13,12,13,
        154,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,174,8,15,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,3,17,183,8,17,1,18,1,18,1,18,1,18,3,18,189,8,18,1,19,1,
        19,3,19,193,8,19,1,20,1,20,1,20,1,20,1,21,3,21,200,8,21,1,21,1,21,
        3,21,204,8,21,1,22,1,22,1,22,3,22,209,8,22,1,22,1,22,1,22,1,23,1,
        23,1,23,5,23,217,8,23,10,23,12,23,220,9,23,1,23,0,0,24,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,4,1,0,
        7,8,1,0,10,12,2,0,31,31,33,33,1,0,13,14,220,0,48,1,0,0,0,2,67,1,
        0,0,0,4,81,1,0,0,0,6,83,1,0,0,0,8,85,1,0,0,0,10,90,1,0,0,0,12,96,
        1,0,0,0,14,98,1,0,0,0,16,100,1,0,0,0,18,116,1,0,0,0,20,118,1,0,0,
        0,22,122,1,0,0,0,24,135,1,0,0,0,26,148,1,0,0,0,28,159,1,0,0,0,30,
        167,1,0,0,0,32,177,1,0,0,0,34,180,1,0,0,0,36,188,1,0,0,0,38,192,
        1,0,0,0,40,194,1,0,0,0,42,199,1,0,0,0,44,205,1,0,0,0,46,213,1,0,
        0,0,48,49,5,1,0,0,49,50,5,30,0,0,50,54,5,2,0,0,51,53,3,24,12,0,52,
        51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,60,1,0,0,
        0,56,54,1,0,0,0,57,59,3,22,11,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,
        1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,3,0,0,
        64,65,3,2,1,0,65,66,5,4,0,0,66,1,1,0,0,0,67,71,5,5,0,0,68,70,3,4,
        2,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,
        1,0,0,0,73,71,1,0,0,0,74,75,5,6,0,0,75,3,1,0,0,0,76,82,3,8,4,0,77,
        82,3,30,15,0,78,82,3,28,14,0,79,82,3,44,22,0,80,82,3,26,13,0,81,
        76,1,0,0,0,81,77,1,0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,
        0,82,5,1,0,0,0,83,84,7,0,0,0,84,7,1,0,0,0,85,86,5,30,0,0,86,87,5,
        9,0,0,87,88,3,10,5,0,88,89,5,2,0,0,89,9,1,0,0,0,90,94,3,16,8,0,91,
        92,3,12,6,0,92,93,3,16,8,0,93,95,1,0,0,0,94,91,1,0,0,0,94,95,1,0,
        0,0,95,11,1,0,0,0,96,97,7,1,0,0,97,13,1,0,0,0,98,99,7,2,0,0,99,15,
        1,0,0,0,100,105,3,34,17,0,101,102,7,3,0,0,102,104,3,34,17,0,103,
        101,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,
        17,1,0,0,0,107,105,1,0,0,0,108,113,3,20,10,0,109,110,5,15,0,0,110,
        112,3,20,10,0,111,109,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,
        114,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,116,108,1,0,0,0,116,
        117,1,0,0,0,117,19,1,0,0,0,118,119,5,30,0,0,119,120,5,16,0,0,120,
        121,3,6,3,0,121,21,1,0,0,0,122,123,5,17,0,0,123,124,5,30,0,0,124,
        125,5,18,0,0,125,126,3,18,9,0,126,127,5,19,0,0,127,129,5,20,0,0,
        128,130,3,24,12,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,
        0,131,132,3,2,1,0,132,133,5,21,0,0,133,134,5,2,0,0,134,23,1,0,0,
        0,135,136,5,22,0,0,136,141,5,30,0,0,137,138,5,15,0,0,138,140,5,30,
        0,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,
        0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,16,0,0,145,146,3,6,
        3,0,146,147,5,2,0,0,147,25,1,0,0,0,148,149,5,23,0,0,149,152,5,18,
        0,0,150,153,3,10,5,0,151,153,5,34,0,0,152,150,1,0,0,0,152,151,1,
        0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,156,1,
        0,0,0,156,157,5,19,0,0,157,158,5,2,0,0,158,27,1,0,0,0,159,160,5,
        24,0,0,160,161,3,2,1,0,161,162,5,25,0,0,162,163,5,18,0,0,163,164,
        3,10,5,0,164,165,5,19,0,0,165,166,5,2,0,0,166,29,1,0,0,0,167,168,
        5,26,0,0,168,169,5,18,0,0,169,170,3,10,5,0,170,171,5,19,0,0,171,
        173,3,2,1,0,172,174,3,32,16,0,173,172,1,0,0,0,173,174,1,0,0,0,174,
        175,1,0,0,0,175,176,5,2,0,0,176,31,1,0,0,0,177,178,5,27,0,0,178,
        179,3,2,1,0,179,33,1,0,0,0,180,182,3,38,19,0,181,183,3,36,18,0,182,
        181,1,0,0,0,182,183,1,0,0,0,183,35,1,0,0,0,184,185,5,28,0,0,185,
        189,3,34,17,0,186,187,5,29,0,0,187,189,3,34,17,0,188,184,1,0,0,0,
        188,186,1,0,0,0,189,37,1,0,0,0,190,193,3,40,20,0,191,193,3,42,21,
        0,192,190,1,0,0,0,192,191,1,0,0,0,193,39,1,0,0,0,194,195,5,18,0,
        0,195,196,3,10,5,0,196,197,5,19,0,0,197,41,1,0,0,0,198,200,7,3,0,
        0,199,198,1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,204,5,30,0,
        0,202,204,3,14,7,0,203,201,1,0,0,0,203,202,1,0,0,0,204,43,1,0,0,
        0,205,206,5,30,0,0,206,208,5,18,0,0,207,209,3,46,23,0,208,207,1,
        0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,211,5,19,0,0,211,212,5,
        2,0,0,212,45,1,0,0,0,213,218,3,10,5,0,214,215,5,15,0,0,215,217,3,
        10,5,0,216,214,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,
        0,0,0,219,47,1,0,0,0,220,218,1,0,0,0,20,54,60,71,81,94,105,113,116,
        129,141,152,154,173,182,188,192,199,203,208,218
    ]

class baby_duck_grammarParser ( Parser ):

    grammarFileName = "baby_duck_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'{'", "'}'", "'int'", "'float'", "'='", "'<'", "'>'", 
                     "'!='", "'+'", "'-'", "','", "':'", "'void'", "'('", 
                     "')'", "'['", "']'", "'var'", "'print'", "'while'", 
                     "'do'", "'if'", "'else'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS", "FLOAT", 
                      "STRING" ]

    RULE_program = 0
    RULE_body = 1
    RULE_statement = 2
    RULE_type = 3
    RULE_assign = 4
    RULE_expression = 5
    RULE_rel_op = 6
    RULE_cte = 7
    RULE_exp = 8
    RULE_f_param_list = 9
    RULE_f_param_list_helper = 10
    RULE_funcs = 11
    RULE_vars = 12
    RULE_print = 13
    RULE_cycle = 14
    RULE_condition = 15
    RULE_condition_else = 16
    RULE_term = 17
    RULE_term_helper = 18
    RULE_factor = 19
    RULE_factor_expr = 20
    RULE_factor_op = 21
    RULE_f_call = 22
    RULE_f_call_helper = 23

    ruleNames =  [ "program", "body", "statement", "type", "assign", "expression", 
                   "rel_op", "cte", "exp", "f_param_list", "f_param_list_helper", 
                   "funcs", "vars", "print", "cycle", "condition", "condition_else", 
                   "term", "term_helper", "factor", "factor_expr", "factor_op", 
                   "f_call", "f_call_helper" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    ID=30
    INT=31
    WS=32
    FLOAT=33
    STRING=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.VarsContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.VarsContext,i)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.FuncsContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.FuncsContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = baby_duck_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(baby_duck_grammarParser.T__0)
            self.state = 49
            self.match(baby_duck_grammarParser.ID)
            self.state = 50
            self.match(baby_duck_grammarParser.T__1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 51
                self.vars_()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 57
                self.funcs()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(baby_duck_grammarParser.T__2)
            self.state = 64
            self.body()
            self.state = 65
            self.match(baby_duck_grammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = baby_duck_grammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(baby_duck_grammarParser.T__4)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1166016512) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(baby_duck_grammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.PrintContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = baby_duck_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = baby_duck_grammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = baby_duck_grammarParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(baby_duck_grammarParser.ID)
            self.state = 86
            self.match(baby_duck_grammarParser.T__8)
            self.state = 87
            self.expression()
            self.state = 88
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.ExpContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Rel_opContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = baby_duck_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.exp()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0):
                self.state = 91
                self.rel_op()
                self.state = 92
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_rel_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_op" ):
                listener.enterRel_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_op" ):
                listener.exitRel_op(self)




    def rel_op(self):

        localctx = baby_duck_grammarParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(baby_duck_grammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(baby_duck_grammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = baby_duck_grammarParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==31 or _la==33):
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.TermContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.TermContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = baby_duck_grammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.term()

            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 101
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 102
                    self.term() 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_param_list_helper(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.F_param_list_helperContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.F_param_list_helperContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_param_list" ):
                listener.enterF_param_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_param_list" ):
                listener.exitF_param_list(self)




    def f_param_list(self):

        localctx = baby_duck_grammarParser.F_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_f_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 108
                self.f_param_list_helper()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 109
                    self.match(baby_duck_grammarParser.T__14)
                    self.state = 110
                    self.f_param_list_helper()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_param_list_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TypeContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_param_list_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_param_list_helper" ):
                listener.enterF_param_list_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_param_list_helper" ):
                listener.exitF_param_list_helper(self)




    def f_param_list_helper(self):

        localctx = baby_duck_grammarParser.F_param_list_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_f_param_list_helper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(baby_duck_grammarParser.ID)
            self.state = 119
            self.match(baby_duck_grammarParser.T__15)
            self.state = 120
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def f_param_list(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_param_listContext,0)


        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def vars_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.VarsContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = baby_duck_grammarParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(baby_duck_grammarParser.T__16)
            self.state = 123
            self.match(baby_duck_grammarParser.ID)
            self.state = 124
            self.match(baby_duck_grammarParser.T__17)
            self.state = 125
            self.f_param_list()
            self.state = 126
            self.match(baby_duck_grammarParser.T__18)
            self.state = 127
            self.match(baby_duck_grammarParser.T__19)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 128
                self.vars_()


            self.state = 131
            self.body()
            self.state = 132
            self.match(baby_duck_grammarParser.T__20)
            self.state = 133
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(baby_duck_grammarParser.ID)
            else:
                return self.getToken(baby_duck_grammarParser.ID, i)

        def type_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TypeContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = baby_duck_grammarParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(baby_duck_grammarParser.T__21)
            self.state = 136
            self.match(baby_duck_grammarParser.ID)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 137
                self.match(baby_duck_grammarParser.T__14)
                self.state = 138
                self.match(baby_duck_grammarParser.ID)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(baby_duck_grammarParser.T__15)
            self.state = 145
            self.type_()
            self.state = 146
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(baby_duck_grammarParser.STRING)
            else:
                return self.getToken(baby_duck_grammarParser.STRING, i)

        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = baby_duck_grammarParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(baby_duck_grammarParser.T__22)
            self.state = 149
            self.match(baby_duck_grammarParser.T__17)
            self.state = 152 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13, 14, 18, 30, 31, 33]:
                    self.state = 150
                    self.expression()
                    pass
                elif token in [34]:
                    self.state = 151
                    self.match(baby_duck_grammarParser.STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28991315968) != 0)):
                    break

            self.state = 156
            self.match(baby_duck_grammarParser.T__18)
            self.state = 157
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = baby_duck_grammarParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(baby_duck_grammarParser.T__23)
            self.state = 160
            self.body()
            self.state = 161
            self.match(baby_duck_grammarParser.T__24)
            self.state = 162
            self.match(baby_duck_grammarParser.T__17)
            self.state = 163
            self.expression()
            self.state = 164
            self.match(baby_duck_grammarParser.T__18)
            self.state = 165
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def condition_else(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Condition_elseContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = baby_duck_grammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(baby_duck_grammarParser.T__25)
            self.state = 168
            self.match(baby_duck_grammarParser.T__17)
            self.state = 169
            self.expression()
            self.state = 170
            self.match(baby_duck_grammarParser.T__18)
            self.state = 171
            self.body()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 172
                self.condition_else()


            self.state = 175
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_condition_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_else" ):
                listener.enterCondition_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_else" ):
                listener.exitCondition_else(self)




    def condition_else(self):

        localctx = baby_duck_grammarParser.Condition_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(baby_duck_grammarParser.T__26)
            self.state = 178
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.FactorContext,0)


        def term_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Term_helperContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = baby_duck_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.factor()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28 or _la==29:
                self.state = 181
                self.term_helper()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TermContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_term_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_helper" ):
                listener.enterTerm_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_helper" ):
                listener.exitTerm_helper(self)




    def term_helper(self):

        localctx = baby_duck_grammarParser.Term_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term_helper)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(baby_duck_grammarParser.T__27)
                self.state = 185
                self.term()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(baby_duck_grammarParser.T__28)
                self.state = 187
                self.term()
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor_expr(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Factor_exprContext,0)


        def factor_op(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Factor_opContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = baby_duck_grammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.factor_expr()
                pass
            elif token in [13, 14, 30, 31, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.factor_op()
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


    class Factor_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_factor_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_expr" ):
                listener.enterFactor_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_expr" ):
                listener.exitFactor_expr(self)




    def factor_expr(self):

        localctx = baby_duck_grammarParser.Factor_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_factor_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(baby_duck_grammarParser.T__17)
            self.state = 195
            self.expression()
            self.state = 196
            self.match(baby_duck_grammarParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.CteContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_factor_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_op" ):
                listener.enterFactor_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_op" ):
                listener.exitFactor_op(self)




    def factor_op(self):

        localctx = baby_duck_grammarParser.Factor_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13 or _la==14:
                self.state = 198
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 201
                self.match(baby_duck_grammarParser.ID)
                pass
            elif token in [31, 33]:
                self.state = 202
                self.cte()
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


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def f_call_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_call_helperContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = baby_duck_grammarParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(baby_duck_grammarParser.ID)
            self.state = 206
            self.match(baby_duck_grammarParser.T__17)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 11811446784) != 0):
                self.state = 207
                self.f_call_helper()


            self.state = 210
            self.match(baby_duck_grammarParser.T__18)
            self.state = 211
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_call_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call_helper" ):
                listener.enterF_call_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call_helper" ):
                listener.exitF_call_helper(self)




    def f_call_helper(self):

        localctx = baby_duck_grammarParser.F_call_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_f_call_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expression()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 214
                self.match(baby_duck_grammarParser.T__14)
                self.state = 215
                self.expression()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





