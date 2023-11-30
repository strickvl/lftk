from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class ReadTimeFormula(FoundationCollector):
    """ReadTimeFormula

    Parent class for features that are in the 'readtimeformula' family.
    """

    def reading_time_for_fast_readers(self) -> float:
        """
        returns value of (total number of words / 300)
        """
        try:
            return self.reading_time_for_fast_readers_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            self.reading_time_for_fast_readers_ = safe_division(
                total_number_of_words_, 300
            )
            # Revert back to user options
            self.options = original_options
        return self.reading_time_for_fast_readers_
    
    def reading_time_for_average_readers(self) -> float:
        """
        returns value of (total number of words / 300)
        """
        try:
            return self.reading_time_for_average_readers_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            self.reading_time_for_average_readers_ = safe_division(
                total_number_of_words_, 240
            )
            # Revert back to user options
            self.options = original_options
        return self.reading_time_for_average_readers_

    def reading_time_for_slow_readers(self) -> float:
        """
        returns value of (total number of words / 300)
        """
        try:
            return self.reading_time_for_slow_readers_
        except AttributeError:
            # Override user options
            original_options = self.options
            self.options['stop_words'] = True
            self.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = FoundationCollector.total_number_of_words(self)
            self.reading_time_for_slow_readers_ = safe_division(
                total_number_of_words_, 175
            )
            # Revert back to user options
            self.options = original_options
        return self.reading_time_for_slow_readers_