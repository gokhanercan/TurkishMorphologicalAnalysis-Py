from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag


class InflectionalGroup:
    __IG: list
    tags = ["Noun", "Adv", "Adj", "Verb", "A1sg",
            "A2sg", "A3sg", "A1Pl", "A2pl", "A3pl",
            "P1sg", "P2sg", "P3sg", "P1Pl", "P2pl",
            "P3pl", "Prop", "Pnon", "Nom", "With",
            "Without", "Acc", "Dat", "Gen", "Abl",
            "Zero", "Able", "Neg", "Past",
            "Conj", "Det", "Dup", "Interj", "Num",
            "PostP", "Punc", "Ques", "Agt", "ByDoingSo",
            "Card", "Caus", "DemonsP", "Distrib", "FitFor",
            "FutPart", "Inf", "Ness", "Ord", "Pass",
            "PastPart", "PresPart", "QuesP", "QuantP", "Range",
            "Ratio", "Real", "Recip", "Reflex", "ReflexP",
            "Time", "When", "While", "WithoutHavingDoneSo", "PCAbl",
            "PCAcc", "PCDat", "PCGen", "PCIns", "PCNom",
            "Acquire", "ActOf", "AfterDoingSo", "Almost", "As",
            "AsIf", "Become", "EverSince", "FeelLike", "Hastily",
            "InBetween", "JustLike", "Ly", "NotAbleState", "Related",
            "Repeat", "Since", "SinceDoingSo", "Start", "Stay",
            "Equ", "Ins", "Aor", "Desr", "Fut",
            "Imp", "Narr", "Neces", "Opt", "Past",
            "Pres", "Prog1", "Prog2", "Cond", "Cop",
            "Pos", "Pron", "Loc", "Rel", "Demons",
            "Inf2", "Inf3", "BSTag", "ESTag", "BTTag",
            "ETTag", "BDTag", "EDTag", "Inf1", "AsLongAs",
            "Dist", "Adamantly", "Percent", "WithoutBeingAbleToHaveDoneSo", "Dim",
            "Pers", "Fraction", "Hashtag", "Email", "Date"]
    morphotags = [MorphologicalTag.NOUN, MorphologicalTag.ADVERB, MorphologicalTag.ADJECTIVE,
                  MorphologicalTag.VERB, MorphologicalTag.A1SG, MorphologicalTag.A2SG, MorphologicalTag.A3SG,
                  MorphologicalTag.A1PL,
                  MorphologicalTag.A2PL, MorphologicalTag.A3PL, MorphologicalTag.P1SG, MorphologicalTag.P2SG,
                  MorphologicalTag.P3SG, MorphologicalTag.P1PL,
                  MorphologicalTag.P2PL, MorphologicalTag.P3PL, MorphologicalTag.PROPERNOUN, MorphologicalTag.PNON,
                  MorphologicalTag.NOMINATIVE,
                  MorphologicalTag.WITH, MorphologicalTag.WITHOUT, MorphologicalTag.ACCUSATIVE, MorphologicalTag.DATIVE,
                  MorphologicalTag.GENITIVE,
                  MorphologicalTag.ABLATIVE, MorphologicalTag.ZERO, MorphologicalTag.ABLE, MorphologicalTag.NEGATIVE,
                  MorphologicalTag.PASTTENSE,
                  MorphologicalTag.CONJUNCTION, MorphologicalTag.DETERMINER, MorphologicalTag.DUPLICATION,
                  MorphologicalTag.INTERJECTION, MorphologicalTag.NUMBER,
                  MorphologicalTag.POSTPOSITION, MorphologicalTag.PUNCTUATION, MorphologicalTag.QUESTION,
                  MorphologicalTag.AGENT, MorphologicalTag.BYDOINGSO,
                  MorphologicalTag.CARDINAL, MorphologicalTag.CAUSATIVE, MorphologicalTag.DEMONSTRATIVEPRONOUN,
                  MorphologicalTag.DISTRIBUTIVE, MorphologicalTag.FITFOR,
                  MorphologicalTag.FUTUREPARTICIPLE, MorphologicalTag.INFINITIVE, MorphologicalTag.NESS,
                  MorphologicalTag.ORDINAL, MorphologicalTag.PASSIVE,
                  MorphologicalTag.PASTPARTICIPLE, MorphologicalTag.PRESENTPARTICIPLE, MorphologicalTag.QUESTIONPRONOUN,
                  MorphologicalTag.QUANTITATIVEPRONOUN, MorphologicalTag.RANGE,
                  MorphologicalTag.RATIO, MorphologicalTag.REAL, MorphologicalTag.RECIPROCAL,
                  MorphologicalTag.REFLEXIVE, MorphologicalTag.REFLEXIVEPRONOUN,
                  MorphologicalTag.TIME, MorphologicalTag.WHEN, MorphologicalTag.WHILE,
                  MorphologicalTag.WITHOUTHAVINGDONESO, MorphologicalTag.PCABLATIVE,
                  MorphologicalTag.PCACCUSATIVE, MorphologicalTag.PCDATIVE, MorphologicalTag.PCGENITIVE,
                  MorphologicalTag.PCINSTRUMENTAL, MorphologicalTag.PCNOMINATIVE,
                  MorphologicalTag.ACQUIRE, MorphologicalTag.ACTOF, MorphologicalTag.AFTERDOINGSO,
                  MorphologicalTag.ALMOST, MorphologicalTag.AS,
                  MorphologicalTag.ASIF, MorphologicalTag.BECOME, MorphologicalTag.EVERSINCE, MorphologicalTag.FEELLIKE,
                  MorphologicalTag.HASTILY,
                  MorphologicalTag.INBETWEEN, MorphologicalTag.JUSTLIKE, MorphologicalTag.LY,
                  MorphologicalTag.NOTABLESTATE, MorphologicalTag.RELATED,
                  MorphologicalTag.REPEAT, MorphologicalTag.SINCE, MorphologicalTag.SINCEDOINGSO,
                  MorphologicalTag.START, MorphologicalTag.STAY,
                  MorphologicalTag.EQUATIVE, MorphologicalTag.INSTRUMENTAL, MorphologicalTag.AORIST,
                  MorphologicalTag.DESIRE, MorphologicalTag.FUTURE,
                  MorphologicalTag.IMPERATIVE, MorphologicalTag.NARRATIVE, MorphologicalTag.NECESSITY,
                  MorphologicalTag.OPTATIVE, MorphologicalTag.PAST,
                  MorphologicalTag.PRESENT, MorphologicalTag.PROGRESSIVE1, MorphologicalTag.PROGRESSIVE2,
                  MorphologicalTag.CONDITIONAL, MorphologicalTag.COPULA,
                  MorphologicalTag.POSITIVE, MorphologicalTag.PRONOUN, MorphologicalTag.LOCATIVE,
                  MorphologicalTag.RELATIVE, MorphologicalTag.DEMONSTRATIVE,
                  MorphologicalTag.INFINITIVE2, MorphologicalTag.INFINITIVE3, MorphologicalTag.BEGINNINGOFSENTENCE,
                  MorphologicalTag.ENDOFSENTENCE, MorphologicalTag.BEGINNINGOFTITLE,
                  MorphologicalTag.ENDOFTITLE, MorphologicalTag.BEGINNINGOFDOCUMENT, MorphologicalTag.ENDOFDOCUMENT,
                  MorphologicalTag.INFINITIVE, MorphologicalTag.ASLONGAS,
                  MorphologicalTag.DISTRIBUTIVE, MorphologicalTag.ADAMANTLY, MorphologicalTag.PERCENT,
                  MorphologicalTag.WITHOUTBEINGABLETOHAVEDONESO, MorphologicalTag.DIMENSION,
                  MorphologicalTag.PERSONALPRONOUN, MorphologicalTag.FRACTION, MorphologicalTag.HASHTAG,
                  MorphologicalTag.EMAIL, MorphologicalTag.DATE]

    """
    A constructor of InflectionalGroup class which initializes the IG list by parsing given input
    String IG by + and calling the getMorphologicalTag method with these substrings. If getMorphologicalTag method 
    returns a tag, it adds this tag to the IG list.

    PARAMETERS
    ----------
    IG : str
        String input.
    """
    def __init__(self, IG: str):
        self.__IG = []
        st = IG
        while "+" in st:
            morphologicalTag = st[:st.index("+")]
            tag = InflectionalGroup.getMorphologicalTag(morphologicalTag)
            if tag is not None:
                self.__IG.append(tag)
            else:
                print("Morphological Tag " + morphologicalTag + " not found")
            st = st[st.index("+") + 1:]
        morphologicalTag = st
        tag = InflectionalGroup.getMorphologicalTag(morphologicalTag)
        if tag is not None:
            self.__IG.append(tag)
        else:
            print("Morphological Tag " + morphologicalTag + " not found")

    """
    The getMorphologicalTag method takes a String tag as an input and if the input matches with one of the elements of
    tags array, it then gets the morphoTags of this tag and returns it.

    PARAMETERS
    ----------
    tag : str
        String to get morphoTags from.
        
    RETURNS
    -------
    MorphologicalTag
        morphoTags if found, None otherwise.
    """
    def getMorphologicalTag(tag: str) -> MorphologicalTag:
        for j in range(len(InflectionalGroup.tags)):
            if tag.upper() == InflectionalGroup.tags[j].upper():
                return InflectionalGroup.morphotags[j]
        return None

    """
    The getTag method takes a MorphologicalTag type tag as an input and returns its corresponding tag from tags array.

    PARAMETERS
    ----------
    tag : MorphologicalTag
        MorphologicalTag type input to find tag from.
        
    RETURNS
    -------
    str
        Tag if found, None otherwise.
    """
    def getTagString(tag: MorphologicalTag) -> str:
        for j in range(len(InflectionalGroup.morphotags)):
            if tag == InflectionalGroup.morphotags[j]:
                return InflectionalGroup.tags[j].upper()
        return None

    """
    Another getTag method which takes index as an input and returns the corresponding tag from IG {@link ArrayList}.

    PARAMETERS
    ----------
    index : int
        index to get tag.
        
    RETURNS
    -------
    MorphologicalTag
        tag at input index.
    """
    def getTag(self, index: int) -> MorphologicalTag:
        return self.__IG[index]

    """
    The size method returns the size of the IG list.

    RETURNS
    -------
    int
        the size of the IG list.
    """
    def size(self) -> int:
        return len(self.__IG)

    """
    Overridden toString method to return resulting tags in IG list.

    RETURNS
    -------
    str
        String result.
    """
    def __str__(self) -> str:
        result = InflectionalGroup.getTagString(self.__IG[0])
        for i in range(1, len(self.__IG)):
            result = result + "+" + InflectionalGroup.getTagString(self.__IG[i])
        return result

    """
    The containsCase method loops through the tags in IG list and finds out the tags of the NOMINATIVE,
    ACCUSATIVE, DATIVE, LOCATIVE or ABLATIVE cases.

    RETURNS
    -------
    MorphologicalTag
        tag which holds the condition.
    """
    def containsCase(self) -> MorphologicalTag:
        for tag in self.__IG:
            if tag == MorphologicalTag.NOMINATIVE or tag == MorphologicalTag.ACCUSATIVE or \
                    tag == MorphologicalTag.DATIVE or tag == MorphologicalTag.LOCATIVE or \
                    tag == MorphologicalTag.ABLATIVE:
                return tag
        return None

    """
    The containsPlural method loops through the tags in IG list and checks whether the tags are from
    the agreement plural or possessive plural, i.e A1PL, A2PL, A3PL, P1PL, P2PL and P3PL.

    RETURNS
    -------
    bool
        True if the tag is plural, False otherwise.
    """
    def containsPlural(self) -> bool:
        for tag in self.__IG:
            if tag == MorphologicalTag.A1PL or tag == MorphologicalTag.A2PL or tag == MorphologicalTag.A3PL or \
                    tag == MorphologicalTag.P1PL or tag == MorphologicalTag.P2PL or tag == MorphologicalTag.P3PL:
                return True
        return False

    """
    The containsTag method takes a MorphologicalTag type tag as an input and loops through the tags in
    IG list and returns true if the input matches with on of the tags in the IG.

    PARAMETERS
    ----------
    tag : MorphologicalTag
        MorphologicalTag type input to search for.
        
    RETURNS
    -------
    bool
        True if tag matches with the tag in IG, False otherwise.
    """
    def containsTag(self, tag: MorphologicalTag) -> bool:
        for currentTag in self.__IG:
            if tag == currentTag:
                return True
        return False

    """
    The containsPossessive method loops through the tags in IG list and returns true if the tag in IG is
    one of the possessives: P1PL, P1SG, P2PL, P2SG, P3PL AND P3SG.

    RETURNS
    -------
    bool
        True if it contains possessive tag, False otherwise.
    """
    def containsPossessive(self) -> bool:
        for tag in self.__IG:
            if tag == MorphologicalTag.P1SG or tag == MorphologicalTag.P1PL or tag == MorphologicalTag.P2SG or \
                    tag == MorphologicalTag.P2PL or tag == MorphologicalTag.P3SG or tag == MorphologicalTag.P3PL:
                return True
        return False
