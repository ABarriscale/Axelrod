from cooperator import *
from defector import *
from grudger import *
from rand import *
from titfortat import *
from gobymajority import *
from gobyrecent import *
from alternator import *
from grumpy import *
from averagecopier import *
from grumpy import *
from geller import *
from inverse import *

strategies = [
        Defector,
        Cooperator,
        TitForTat,
        Grudger,
        GoByMajority,
        GoByRecentMajority5,
        GoByRecentMajority10,
        GoByRecentMajority20,
        GoByRecentMajority40,
        Random,
        Alternator,
        Grumpy,
        Inverse,
        AverageCopier,
        ]

#These are strategies that do not follow the rules of Axelrods tournement.
cheating_strategies = [
        Geller,
        ]
