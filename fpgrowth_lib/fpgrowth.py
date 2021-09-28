from optparse import OptionParser
from fpgrowth_lib.utils import *

def fpgrowth(transaksi, minSupRatio, minConf):
    itemSetList = getItemSetList(transaksi)
    frequency = getFrequencyFromList(itemSetList)
    minSup = len(itemSetList) * minSupRatio
    frequentItemset, orderedItemset = Itemset(transaksi, frequency, minSup)
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    if(fpTree == None):
        print('No frequent item set')
    else:
        freqItems = []
        freqItemSet = []
        mineTree(headerTable, minSup, set(), freqItems)
        freqItemSet, rules = associationRule(freqItems, itemSetList, minConf)
        return frequentItemset, orderedItemset, freqItemSet, rules

# def fpgrowthFromFile(fname, minSupRatio, minConf):
#     itemSetList, frequency = getFromFile(fname)
#     minSup = len(itemSetList) * minSupRatio
#     fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
#     if(fpTree == None):
#         print('No frequent item set')
#     else:
#         freqItems = []
#         mineTree(headerTable, minSup, set(), freqItems)
#         rules = associationRule(freqItems, itemSetList, minConf)
#         return freqItems, rules

if __name__ == "__main__":
    optparser = OptionParser()
    # optparser.add_option('-f', '--inputFile',
    #                      dest='inputFile',
    #                      help='CSV filename',
    #                      default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minSup',
                         help='Min support (float)',
                         default=0.5,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minConf',
                         help='Min confidence (float)',
                         default=0.5,
                         type='float')

    (options, args) = optparser.parse_args()

    freqItemSet, rules = fpgrowth(options.minSup, options.minConf)
