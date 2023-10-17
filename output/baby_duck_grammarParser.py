# Generated from ./baby_duck_grammar.g4 by ANTLR 4.13.1
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
        4,1,31,246,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,0,3,0,67,8,
        0,1,0,1,0,1,1,1,1,3,1,73,8,1,1,2,1,2,5,2,77,8,2,10,2,12,2,80,9,2,
        1,2,1,2,1,3,1,3,3,3,86,8,3,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,107,8,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,1,11,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,134,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,143,8,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,5,14,153,8,14,10,14,12,14,156,9,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,3,16,
        170,8,16,1,17,1,17,3,17,174,8,17,1,18,1,18,1,18,3,18,179,8,18,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,195,8,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,3,22,204,8,22,
        1,23,1,23,1,23,1,23,3,23,210,8,23,1,24,1,24,3,24,214,8,24,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,228,8,
        26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,29,1,29,3,29,239,8,29,1,
        30,1,30,1,30,3,30,244,8,30,1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,
        4,1,0,5,6,1,0,8,10,2,0,6,6,29,29,1,0,11,12,239,0,62,1,0,0,0,2,70,
        1,0,0,0,4,74,1,0,0,0,6,83,1,0,0,0,8,92,1,0,0,0,10,94,1,0,0,0,12,
        96,1,0,0,0,14,106,1,0,0,0,16,108,1,0,0,0,18,110,1,0,0,0,20,112,1,
        0,0,0,22,120,1,0,0,0,24,133,1,0,0,0,26,135,1,0,0,0,28,148,1,0,0,
        0,30,161,1,0,0,0,32,169,1,0,0,0,34,171,1,0,0,0,36,175,1,0,0,0,38,
        180,1,0,0,0,40,188,1,0,0,0,42,198,1,0,0,0,44,201,1,0,0,0,46,209,
        1,0,0,0,48,213,1,0,0,0,50,215,1,0,0,0,52,227,1,0,0,0,54,229,1,0,
        0,0,56,234,1,0,0,0,58,236,1,0,0,0,60,240,1,0,0,0,62,63,5,1,0,0,63,
        64,5,28,0,0,64,66,5,2,0,0,65,67,3,28,14,0,66,65,1,0,0,0,66,67,1,
        0,0,0,67,68,1,0,0,0,68,69,3,26,13,0,69,1,1,0,0,0,70,72,3,26,13,0,
        71,73,3,2,1,0,72,71,1,0,0,0,72,73,1,0,0,0,73,3,1,0,0,0,74,78,5,3,
        0,0,75,77,3,8,4,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,
        1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,4,0,0,82,5,1,0,0,0,83,
        85,3,8,4,0,84,86,3,6,3,0,85,84,1,0,0,0,85,86,1,0,0,0,86,7,1,0,0,
        0,87,93,3,12,6,0,88,93,3,40,20,0,89,93,3,38,19,0,90,93,3,54,27,0,
        91,93,3,30,15,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,
        1,0,0,0,92,91,1,0,0,0,93,9,1,0,0,0,94,95,7,0,0,0,95,11,1,0,0,0,96,
        97,5,28,0,0,97,98,5,7,0,0,98,99,3,14,7,0,99,100,5,2,0,0,100,13,1,
        0,0,0,101,107,3,20,10,0,102,103,3,20,10,0,103,104,3,16,8,0,104,105,
        3,20,10,0,105,107,1,0,0,0,106,101,1,0,0,0,106,102,1,0,0,0,107,15,
        1,0,0,0,108,109,7,1,0,0,109,17,1,0,0,0,110,111,7,2,0,0,111,19,1,
        0,0,0,112,117,3,44,22,0,113,114,7,3,0,0,114,116,3,44,22,0,115,113,
        1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,21,1,
        0,0,0,119,117,1,0,0,0,120,121,5,13,0,0,121,122,3,24,12,0,122,123,
        5,14,0,0,123,23,1,0,0,0,124,125,5,28,0,0,125,126,5,15,0,0,126,134,
        3,10,5,0,127,128,5,28,0,0,128,129,5,15,0,0,129,130,3,10,5,0,130,
        131,5,16,0,0,131,132,3,24,12,0,132,134,1,0,0,0,133,124,1,0,0,0,133,
        127,1,0,0,0,134,25,1,0,0,0,135,136,5,17,0,0,136,137,5,28,0,0,137,
        138,5,13,0,0,138,139,3,22,11,0,139,140,5,14,0,0,140,142,5,18,0,0,
        141,143,3,28,14,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,
        0,144,145,3,4,2,0,145,146,5,19,0,0,146,147,5,2,0,0,147,27,1,0,0,
        0,148,149,5,20,0,0,149,154,5,28,0,0,150,151,5,16,0,0,151,153,5,28,
        0,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,
        0,0,155,157,1,0,0,0,156,154,1,0,0,0,157,158,5,15,0,0,158,159,3,10,
        5,0,159,160,5,2,0,0,160,29,1,0,0,0,161,162,5,21,0,0,162,163,5,13,
        0,0,163,164,3,34,17,0,164,165,5,14,0,0,165,166,5,2,0,0,166,31,1,
        0,0,0,167,170,3,14,7,0,168,170,5,31,0,0,169,167,1,0,0,0,169,168,
        1,0,0,0,170,33,1,0,0,0,171,173,3,32,16,0,172,174,3,36,18,0,173,172,
        1,0,0,0,173,174,1,0,0,0,174,35,1,0,0,0,175,176,5,16,0,0,176,178,
        3,32,16,0,177,179,3,36,18,0,178,177,1,0,0,0,178,179,1,0,0,0,179,
        37,1,0,0,0,180,181,5,22,0,0,181,182,3,4,2,0,182,183,5,23,0,0,183,
        184,5,13,0,0,184,185,3,14,7,0,185,186,5,14,0,0,186,187,5,2,0,0,187,
        39,1,0,0,0,188,189,5,24,0,0,189,190,5,13,0,0,190,191,3,14,7,0,191,
        192,5,14,0,0,192,194,3,4,2,0,193,195,3,42,21,0,194,193,1,0,0,0,194,
        195,1,0,0,0,195,196,1,0,0,0,196,197,5,2,0,0,197,41,1,0,0,0,198,199,
        5,25,0,0,199,200,3,4,2,0,200,43,1,0,0,0,201,203,3,48,24,0,202,204,
        3,46,23,0,203,202,1,0,0,0,203,204,1,0,0,0,204,45,1,0,0,0,205,206,
        5,26,0,0,206,210,3,44,22,0,207,208,5,27,0,0,208,210,3,44,22,0,209,
        205,1,0,0,0,209,207,1,0,0,0,210,47,1,0,0,0,211,214,3,50,25,0,212,
        214,3,52,26,0,213,211,1,0,0,0,213,212,1,0,0,0,214,49,1,0,0,0,215,
        216,5,13,0,0,216,217,3,14,7,0,217,218,5,14,0,0,218,51,1,0,0,0,219,
        220,5,11,0,0,220,228,5,28,0,0,221,222,5,11,0,0,222,228,3,18,9,0,
        223,224,5,12,0,0,224,228,5,28,0,0,225,226,5,12,0,0,226,228,3,18,
        9,0,227,219,1,0,0,0,227,221,1,0,0,0,227,223,1,0,0,0,227,225,1,0,
        0,0,228,53,1,0,0,0,229,230,5,13,0,0,230,231,3,56,28,0,231,232,5,
        14,0,0,232,233,5,2,0,0,233,55,1,0,0,0,234,235,3,58,29,0,235,57,1,
        0,0,0,236,238,3,14,7,0,237,239,3,60,30,0,238,237,1,0,0,0,238,239,
        1,0,0,0,239,59,1,0,0,0,240,241,5,16,0,0,241,243,3,14,7,0,242,244,
        3,60,30,0,243,242,1,0,0,0,243,244,1,0,0,0,244,61,1,0,0,0,20,66,72,
        78,85,92,106,117,133,142,154,169,173,178,194,203,209,213,227,238,
        243
    ]

class baby_duck_grammarParser ( Parser ):

    grammarFileName = "baby_duck_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'{'", "'}'", "'int'", 
                     "'float'", "'='", "'<'", "'>'", "'!='", "'+'", "'-'", 
                     "'('", "')'", "':'", "','", "'void'", "'['", "']'", 
                     "'var'", "'print'", "'while'", "'do'", "'if'", "'else'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS", "STRING" ]

    RULE_program = 0
    RULE_funcs_list = 1
    RULE_body = 2
    RULE_statement_list = 3
    RULE_statement = 4
    RULE_type = 5
    RULE_assign = 6
    RULE_expression = 7
    RULE_rel_op = 8
    RULE_cte = 9
    RULE_exp = 10
    RULE_f_param_list = 11
    RULE_f_param_list_helper = 12
    RULE_funcs = 13
    RULE_vars = 14
    RULE_print = 15
    RULE_print_arg = 16
    RULE_print_helper = 17
    RULE_print_helper_inner = 18
    RULE_cycle = 19
    RULE_condition = 20
    RULE_condition_else = 21
    RULE_term = 22
    RULE_term_helper = 23
    RULE_factor = 24
    RULE_factor_expr = 25
    RULE_factor_op = 26
    RULE_f_call = 27
    RULE_f_call_helper = 28
    RULE_expression_list = 29
    RULE_expression_list_helper = 30

    ruleNames =  [ "program", "funcs_list", "body", "statement_list", "statement", 
                   "type", "assign", "expression", "rel_op", "cte", "exp", 
                   "f_param_list", "f_param_list_helper", "funcs", "vars", 
                   "print", "print_arg", "print_helper", "print_helper_inner", 
                   "cycle", "condition", "condition_else", "term", "term_helper", 
                   "factor", "factor_expr", "factor_op", "f_call", "f_call_helper", 
                   "expression_list", "expression_list_helper" ]

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
    ID=28
    INT=29
    WS=30
    STRING=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def funcs(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.FuncsContext,0)


        def vars_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.VarsContext,0)


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
            self.state = 62
            self.match(baby_duck_grammarParser.T__0)
            self.state = 63
            self.match(baby_duck_grammarParser.ID)
            self.state = 64
            self.match(baby_duck_grammarParser.T__1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 65
                self.vars_()


            self.state = 68
            self.funcs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcs_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.FuncsContext,0)


        def funcs_list(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Funcs_listContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_funcs_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs_list" ):
                listener.enterFuncs_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs_list" ):
                listener.exitFuncs_list(self)




    def funcs_list(self):

        localctx = baby_duck_grammarParser.Funcs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcs_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.funcs()
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 71
                self.funcs_list()


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
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(baby_duck_grammarParser.T__2)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 291512320) != 0):
                self.state = 75
                self.statement()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(baby_duck_grammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Statement_listContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = baby_duck_grammarParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.statement()
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 84
                self.statement_list()


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
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.assign()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.condition()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.cycle()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.f_call()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.print_()
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
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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
        self.enterRule(localctx, 12, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(baby_duck_grammarParser.ID)
            self.state = 97
            self.match(baby_duck_grammarParser.T__6)
            self.state = 98
            self.expression()
            self.state = 99
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
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.exp()
                self.state = 103
                self.rel_op()
                self.state = 104
                self.exp()
                pass


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
        self.enterRule(localctx, 16, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==6 or _la==29):
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
        self.enterRule(localctx, 20, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.term()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.term()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def f_param_list_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_param_list_helperContext,0)


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
        self.enterRule(localctx, 22, self.RULE_f_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(baby_duck_grammarParser.T__12)
            self.state = 121
            self.f_param_list_helper()
            self.state = 122
            self.match(baby_duck_grammarParser.T__13)
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


        def f_param_list_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_param_list_helperContext,0)


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
        self.enterRule(localctx, 24, self.RULE_f_param_list_helper)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(baby_duck_grammarParser.ID)
                self.state = 125
                self.match(baby_duck_grammarParser.T__14)
                self.state = 126
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(baby_duck_grammarParser.ID)
                self.state = 128
                self.match(baby_duck_grammarParser.T__14)
                self.state = 129
                self.type_()
                self.state = 130
                self.match(baby_duck_grammarParser.T__15)
                self.state = 131
                self.f_param_list_helper()
                pass


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
        self.enterRule(localctx, 26, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(baby_duck_grammarParser.T__16)
            self.state = 136
            self.match(baby_duck_grammarParser.ID)
            self.state = 137
            self.match(baby_duck_grammarParser.T__12)
            self.state = 138
            self.f_param_list()
            self.state = 139
            self.match(baby_duck_grammarParser.T__13)
            self.state = 140
            self.match(baby_duck_grammarParser.T__17)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 141
                self.vars_()


            self.state = 144
            self.body()
            self.state = 145
            self.match(baby_duck_grammarParser.T__18)
            self.state = 146
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
        self.enterRule(localctx, 28, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(baby_duck_grammarParser.T__19)
            self.state = 149
            self.match(baby_duck_grammarParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 150
                self.match(baby_duck_grammarParser.T__15)
                self.state = 151
                self.match(baby_duck_grammarParser.ID)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(baby_duck_grammarParser.T__14)
            self.state = 158
            self.type_()
            self.state = 159
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

        def print_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Print_helperContext,0)


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
        self.enterRule(localctx, 30, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(baby_duck_grammarParser.T__20)
            self.state = 162
            self.match(baby_duck_grammarParser.T__12)
            self.state = 163
            self.print_helper()
            self.state = 164
            self.match(baby_duck_grammarParser.T__13)
            self.state = 165
            self.match(baby_duck_grammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(baby_duck_grammarParser.STRING, 0)

        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_print_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_arg" ):
                listener.enterPrint_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_arg" ):
                listener.exitPrint_arg(self)




    def print_arg(self):

        localctx = baby_duck_grammarParser.Print_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_print_arg)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.expression()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(baby_duck_grammarParser.STRING)
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


    class Print_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_arg(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Print_argContext,0)


        def print_helper_inner(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Print_helper_innerContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_print_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_helper" ):
                listener.enterPrint_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_helper" ):
                listener.exitPrint_helper(self)




    def print_helper(self):

        localctx = baby_duck_grammarParser.Print_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_print_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.print_arg()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 172
                self.print_helper_inner()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_helper_innerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_arg(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Print_argContext,0)


        def print_helper_inner(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Print_helper_innerContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_print_helper_inner

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_helper_inner" ):
                listener.enterPrint_helper_inner(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_helper_inner" ):
                listener.exitPrint_helper_inner(self)




    def print_helper_inner(self):

        localctx = baby_duck_grammarParser.Print_helper_innerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_print_helper_inner)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(baby_duck_grammarParser.T__15)
            self.state = 176
            self.print_arg()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 177
                self.print_helper_inner()


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
        self.enterRule(localctx, 38, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(baby_duck_grammarParser.T__21)
            self.state = 181
            self.body()
            self.state = 182
            self.match(baby_duck_grammarParser.T__22)
            self.state = 183
            self.match(baby_duck_grammarParser.T__12)
            self.state = 184
            self.expression()
            self.state = 185
            self.match(baby_duck_grammarParser.T__13)
            self.state = 186
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
        self.enterRule(localctx, 40, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(baby_duck_grammarParser.T__23)
            self.state = 189
            self.match(baby_duck_grammarParser.T__12)
            self.state = 190
            self.expression()
            self.state = 191
            self.match(baby_duck_grammarParser.T__13)
            self.state = 192
            self.body()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 193
                self.condition_else()


            self.state = 196
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
        self.enterRule(localctx, 42, self.RULE_condition_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(baby_duck_grammarParser.T__24)
            self.state = 199
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
        self.enterRule(localctx, 44, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.factor()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 202
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
        self.enterRule(localctx, 46, self.RULE_term_helper)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(baby_duck_grammarParser.T__25)
                self.state = 206
                self.term()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(baby_duck_grammarParser.T__26)
                self.state = 208
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
        self.enterRule(localctx, 48, self.RULE_factor)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.factor_expr()
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
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
        self.enterRule(localctx, 50, self.RULE_factor_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(baby_duck_grammarParser.T__12)
            self.state = 216
            self.expression()
            self.state = 217
            self.match(baby_duck_grammarParser.T__13)
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
        self.enterRule(localctx, 52, self.RULE_factor_op)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(baby_duck_grammarParser.T__10)
                self.state = 220
                self.match(baby_duck_grammarParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(baby_duck_grammarParser.T__10)
                self.state = 222
                self.cte()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(baby_duck_grammarParser.T__11)
                self.state = 224
                self.match(baby_duck_grammarParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(baby_duck_grammarParser.T__11)
                self.state = 226
                self.cte()
                pass


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
        self.enterRule(localctx, 54, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(baby_duck_grammarParser.T__12)
            self.state = 230
            self.f_call_helper()
            self.state = 231
            self.match(baby_duck_grammarParser.T__13)
            self.state = 232
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

        def expression_list(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Expression_listContext,0)


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
        self.enterRule(localctx, 56, self.RULE_f_call_helper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def expression_list_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Expression_list_helperContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = baby_duck_grammarParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expression()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 237
                self.expression_list_helper()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_list_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def expression_list_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Expression_list_helperContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_expression_list_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list_helper" ):
                listener.enterExpression_list_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list_helper" ):
                listener.exitExpression_list_helper(self)




    def expression_list_helper(self):

        localctx = baby_duck_grammarParser.Expression_list_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression_list_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(baby_duck_grammarParser.T__15)
            self.state = 241
            self.expression()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 242
                self.expression_list_helper()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





