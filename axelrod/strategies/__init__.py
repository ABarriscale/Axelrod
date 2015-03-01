from alternator import *
from appeaser import *
from averagecopier import *
from cooperator import *
from defector import *
from forgetfulgrudger import *
from forgiver import *
from geller import *
from gobymajority import *
from grudger import *
from grumpy import *
from grumpy import *
from inverse import *
from inversepunisher import *
from mathematicalconstants import *
from mindcontrol import *
from mindreader import *
from oncebitten import *
from oppositegrudger import *
from punisher import *
from qlearner import *
from rand import *
from retaliate import *
from titfortat import *

basic_strategies = [
    Alternator,
    Cooperator,
    Defector,
    Random,
    TitForTat,
]

strategies = basic_strategies + [
    AntiTitForTat,
    Appeaser,
    ArrogantQLearner,
    AverageCopier,
    CautiousQLearner,
    ForgetfulGrudger,
    Forgiver,
    ForgivingTitForTat,
    GoByMajority,
    GoByMajority10,
    GoByMajority20,
    GoByMajority40,
    GoByMajority5,
    Golden,
    Grudger,
    Grumpy,
    HesitantQLearner,
    Inverse,
    InversePunisher,
    LimitedRetaliate,
    OnceBitten,
    OppositeGrudger,
    Pi,
    Punisher,
    Retaliate,
    RiskyQLearner,
    TitFor2Tats,
    TrickyCooperator,
    TrickyDefector,
    TwoTitsForTat,
    e,
]

# These are strategies that do not follow the rules of Axelrods tournament
cheating_strategies = [
    Geller,
    GellerCooperator,
    GellerDefector,
    MindBender,
    MindController,
    MindReader,
    MindWarper,
    ProtectedMindReader,
    ]

all_strategies = strategies + cheating_strategies
