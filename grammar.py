
grammar_vp = r"""
    AP: {<RB|RBR|RBS>?<JJ>}
    NP: {<PDT|DT|PRP\$|AP|NN.*>+}
    NP: {<PRP>}
    PP: {<IN><NP>}
    VP: {<VB.*><RP|RB>?<NP|PP>+}
    """

grammar_np = r"""
    AP: {<RB|RBR|RBS>?<JJ>}
    NP: {<PDT>?<DT|PRP\$|AP><NN.*>+}
    """

def_dets = ['the', 'this', 'that', 'these', 'those', 'my', 'our', 'your', 'his', 'her', 'its', 'their']
