import spacy
from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class AvgWordDiff(FoundationCollector):
    """AvgWordDiff

    Parent class for features that are in the 'avgworddiff' family.
    """

    def average_kuperman_age_of_acquistion_of_words_per_sentence(self) -> float:
        """
        returns value of (total Kuperman score / total number of sentences)
        """
        try:
            return self.average_kuperman_age_of_acquistion_of_words_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_kuperman_age_of_acquistion_of_words_ = (
                FoundationCollector.total_kuperman_age_of_acquistion_of_words(self)
            )
            self.average_kuperman_age_of_acquistion_of_words_per_sentence_ = (
                safe_division(
                    total_kuperman_age_of_acquistion_of_words_,
                    total_number_of_sentences_,
                )
            )
            return self.average_kuperman_age_of_acquistion_of_words_per_sentence_


    def average_kuperman_age_of_acquistion_of_words_per_word(self) -> float:
        """
        returns value of (total Kuperman score / total number of words)
        """
        try:
            return self.average_kuperman_age_of_acquistion_of_words_per_word_
        except AttributeError:
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_kuperman_age_of_acquistion_of_words_ = (
                FoundationCollector.total_kuperman_age_of_acquistion_of_words(self)
            )
            self.average_kuperman_age_of_acquistion_of_words_per_word_ = (
                safe_division(
                    total_kuperman_age_of_acquistion_of_words_,
                    total_number_of_words_,
                )
            )
            return self.average_kuperman_age_of_acquistion_of_words_per_word_
    

    def average_brysbaert_age_of_acquistion_of_words_per_word(self) -> float:
        """
        returns value of (total Brysbaert score / total number of words)
        """
        try:
            return self.average_brysbaert_age_of_acquistion_of_words_per_word_
        except AttributeError:
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_brysbaert_age_of_acquistion_of_words_ = (
                FoundationCollector.total_brysbaert_age_of_acquistion_of_words(
                    self
                )
            )
            self.average_brysbaert_age_of_acquistion_of_words_per_word_ = (
                safe_division(
                    total_brysbaert_age_of_acquistion_of_words_,
                    total_number_of_words_,
                )
            )
            return self.average_brysbaert_age_of_acquistion_of_words_per_word_
    

    def average_brysbaert_age_of_acquistion_of_words_per_sentence(self) -> float:
        """
        returns value of (total Brysbaert score / total number of sentence)
        """
        try:
            return self.average_brysbaert_age_of_acquistion_of_words_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_brysbaert_age_of_acquistion_of_words_ = (
                FoundationCollector.total_brysbaert_age_of_acquistion_of_words(
                    self
                )
            )
            self.average_brysbaert_age_of_acquistion_of_words_per_sentence_ = (
                safe_division(
                    total_brysbaert_age_of_acquistion_of_words_,
                    total_number_of_sentences_,
                )
            )
            return self.average_brysbaert_age_of_acquistion_of_words_per_sentence_

    
    def average_subtlex_us_zipf_of_words_per_word(self) -> float:
        """
        returns value of (total subtlexus zipf score / total number of words)
        """
        try:
            return self.average_subtlex_us_zipf_of_words_per_word_
        except AttributeError:
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_subtlex_us_zipf_of_words_ = (
                FoundationCollector.total_subtlex_us_zipf_of_words(self)
            )
            self.average_subtlex_us_zipf_of_words_per_word_ = safe_division(
                total_subtlex_us_zipf_of_words_, total_number_of_words_
            )
            return self.average_subtlex_us_zipf_of_words_per_word_
    

    def average_subtlex_us_zipf_of_words_per_sentence(self) -> float:
        """
        returns value of (total subtlexus zipf score / total number of sentences)
        """
        try:
            return self.average_subtlex_us_zipf_of_words_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_subtlex_us_zipf_of_words_ = (
                FoundationCollector.total_subtlex_us_zipf_of_words(self)
            )
            self.subtlex_us_zipf_of_words_per_sentence_ = safe_division(
                total_subtlex_us_zipf_of_words_, total_number_of_sentences_
            )
            return self.subtlex_us_zipf_of_words_per_sentence_