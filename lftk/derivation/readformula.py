import math

from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class ReadFormula(FoundationCollector):
    """ReadFormula

    Parent class for features that are in the 'readformula' family.
    """

    def flesch_kincaid_reading_ease(self) -> float:
        """
        returns reading difficulty value from flesch kincaid reading ease formula, where 100.00–90.00->5th grade (Very easy to read), 90.0–80.0->6th grade (Easy to read), 80.0–70.0->7th grade (Fairly easy to read), 70.0–60.0->8th & 9th grade (Plain English, 60.0–50.0->10th to 12th grade (Fairly difficult to read), 50.0–30.0->College (Difficult to read), 30.0–10.0->College graduate (Very difficult to read), 10.0–0.0->Professional (Extremely difficult to read)
        """
        try:
            return self.flesch_kincaid_reading_ease_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_number_of_syllables_ = (
                FoundationCollector.total_number_of_syllables(self)
            )
            average_number_of_words_per_sentence_ = \
                    safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            average_number_of_syllables_per_word_ = \
                    safe_division(
                    total_number_of_syllables_,
                    total_number_of_words_
                )
            # Calculate readability
            self.flesch_kincaid_reading_ease_ = (
                206.835
                - 1.015 * average_number_of_words_per_sentence_
                - 84.6 * average_number_of_syllables_per_word_
            )
            # Revert back to user options
            self.options = original_options
            return self.flesch_kincaid_reading_ease_
    
    def flesch_kincaid_grade_level(self) -> float:
        """
        returns reading difficulty value that corresponds to US grade level
        """
        try:
            return self.flesch_kincaid_grade_level_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_number_of_syllables_ = (
                FoundationCollector.total_number_of_syllables(self)
            )
            average_number_of_words_per_sentence_ = \
                    safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            average_number_of_syllables_per_word_ = \
                    safe_division(
                    total_number_of_syllables_,
                    total_number_of_words_
                )
            # Calculate readability
            self.flesch_kincaid_grade_level_ = (
                0.39 * average_number_of_words_per_sentence_
                + 11.8 * average_number_of_syllables_per_word_
                - 15.59
            )
            # Revert back to user options
            self.options = original_options
            return self.flesch_kincaid_grade_level_
    
    def gunning_fog_index(self) -> float:
        """
        returns gunning fog index, where 17->College graduate, 16->College senior, 15->College junior, 14->College sophomore, 13->College freshman, 12->High school senior, 11->High school junior, 10->High school sophomore, 9->High school freshman, 8->Eighth grade, 7->Seventh grade, 6->Sixth grade
        """
        try:
            return self.gunning_fog_index_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_number_of_words_more_than_two_syllables_ = (
                FoundationCollector.total_number_of_words_more_than_two_syllables(
                    self
                )
            )
            average_number_of_words_per_sentence_ = \
                    safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            average_number_of_words_more_than_two_syllables_per_word_ = \
                    safe_division(
                    total_number_of_words_more_than_two_syllables_,
                    total_number_of_words_
                )
            # Calculate readability
            self.gunning_fog_index_ = 0.4 * (
                average_number_of_words_per_sentence_
                + 100 * average_number_of_words_more_than_two_syllables_per_word_
            )
            # Revert back to user options
            self.options = original_options
            return self.gunning_fog_index_
    
    def smog_index(self) -> float:
        """
        returns reading difficulty value that corresponds to US grade level
        """
        try:
            return self.smog_index_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            total_number_of_words_more_than_three_syllables_ = FoundationCollector.total_number_of_words_more_than_three_syllables(
                self
            )
            # Calculate readability
            self.smog_index_ = 1.0430 * math.sqrt(
                total_number_of_words_more_than_three_syllables_
                * safe_division(30, total_number_of_sentences_)
            )
            # Revert back to user options
            self.options = original_options
            return self.smog_index_

    def coleman_liau_index(self) -> float:
        """
        returns reading difficulty value that corresponds to US grade level
        """
        try:
            return self.coleman_liau_index_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_characters_ = (
                FoundationCollector.total_number_of_characters(self)
            )
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            average_number_of_letters_per_100words_ = \
                    safe_division(
                    total_number_of_characters_,
                    total_number_of_words_
                ) * 100
            average_number_of_sentences_per_100words_ = \
                    safe_division(
                    total_number_of_sentences_,
                    total_number_of_words_
                ) * 100
            # Calculate readability
            self.coleman_liau_index_ = (
                0.0588 * average_number_of_letters_per_100words_
                - 0.296 * average_number_of_sentences_per_100words_
                - 15.8
            )
            # Revert back to user options
            self.options = original_options
            return self.coleman_liau_index_
    
    def automated_readability_index(self) -> float:
        """
        returns reading difficulty value that corresponds to US grade level
        """
        try:
            return self.automated_readability_index_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_characters_ = (
                FoundationCollector.total_number_of_characters(self)
            )
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            total_number_of_sentences_ = (
                FoundationCollector.total_number_of_sentences(self)
            )
            average_number_of_letters_per_word_ = \
                    safe_division(
                    total_number_of_characters_,
                    total_number_of_words_
                )
            average_number_of_words_per_sentence_ = \
                    safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            # Calculate readability
            self.automated_readability_index_ = (
                4.71 * average_number_of_letters_per_word_
                + 0.5 * average_number_of_words_per_sentence_
                - 21.43
            )
            # Revert back to user options
            self.options = original_options
            return self.automated_readability_index_