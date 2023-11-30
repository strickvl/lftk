import pandas as pd

from lftk.utils import get_pandas_row, safe_division

class WordDiff:
    """WordDiff

    Parent class for features that are in the 'worddiff' family.
    """

    def total_kuperman_age_of_acquistion_of_words(self) -> float:
        """
        returns the total value of total Kuperman score (adds up all words' Kuperman difficulty score)
        """
        try:
            return self.total_kuperman_age_of_acquistion_of_words_
        except AttributeError:
            # Load databse
            database = pd.read_csv(self.paths['AOA_KUP_PATH'])
            # Iterate doc
            doc_total = 0
            for token in self.doc:
                row = get_pandas_row(database, 'Word', token.lemma_)
                try:
                    doc_total += float(row[0]['Rating.Mean'])
                except IndexError:
                    pass
            self.total_kuperman_age_of_acquistion_of_words_ = doc_total
            return self.total_kuperman_age_of_acquistion_of_words_


    def total_brysbaert_age_of_acquistion_of_words(self) -> float:
        """
        returns the total value of total Brysbaert score (adds up all words' Brysbaert difficulty score)
        """
        try:
            return self.total_brysbaert_age_of_acquistion_of_words_
        except AttributeError:
            database = pd.read_csv(self.paths['AOA_BRY_PATH'])
            doc_total = 0
            for token in self.doc:
                rows = get_pandas_row(database, 'WORD', token.lemma_)
                aoa_by_token_meaning = []
                for row in rows:
                    try:
                        aoa_by_token_meaning.append(row['AoAtestbased'])
                    except IndexError:
                        pass
                doc_total += safe_division(
                    sum(aoa_by_token_meaning),len(aoa_by_token_meaning)
                    )
            self.total_brysbaert_age_of_acquistion_of_words_ = doc_total
            return self.total_brysbaert_age_of_acquistion_of_words_

    
    def total_subtlex_us_zipf_of_words(self) -> float:
        """
        returns the total value of total SubtlexUS frequency score (adds up all words' zipf score from SubtlexUS)
        """
        try:
            return self.total_subtlex_us_zipf_of_words_
        except AttributeError:
            database = pd.read_csv(self.paths['SUBTLEX_US_PATH'])
            doc_total = 0
            for token in self.doc:
                row = get_pandas_row(database, 'Word', token.text.lower())
                try:
                    doc_total += float(row[0]['Zipf-value'])
                except IndexError:
                    pass
            self.total_subtlex_us_zipf_of_words_ = doc_total
            return self.total_subtlex_us_zipf_of_words_
