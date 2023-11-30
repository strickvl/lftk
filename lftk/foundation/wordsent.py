class WordSent:
    """WordSent

    Parent class for features that are in the 'wordsent' family.
    """

    def total_number_of_words(self) -> int:
        """
        returns the number of words
        """
        try:
            return self.total_number_of_words_
        except AttributeError:   
            token_list = list(self.doc)
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not self.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Calculate and save result
            self.total_number_of_words_ = len(token_list)
            return self.total_number_of_words_
    
    def total_number_of_stop_words(self) -> int:
        """
        returns the number of stop words
        """
        try:
            return self.total_number_of_stop_words_
        except AttributeError:   
            token_list = [token for token in SE.doc if token.is_stop == True]
            # Calculate and save result
            self.total_number_of_stop_words_ = len(token_list)
            return self.total_number_of_stop_words_ 
    
    def total_number_of_punctuations(self) -> int:
        """
        returns the number of punctuations
        """
        try:
            return self.total_number_of_punctuations_
        except AttributeError:   
            token_list = [token for token in SE.doc if token.is_punct == True]
            # Calculate and save result
            self.total_number_of_punctuations_ = len(token_list)
            return self.total_number_of_punctuations_ 
    
    def total_number_of_syllables(self) -> int:
        """
        returns the number of syllables
        """
        try:
            return self.total_number_of_syllables_
        except AttributeError:
            self.total_number_of_syllables_ = 0
            # always remove punctuations
            token_list = [token for token in SE.doc if token.is_punct != True]
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            # start counting syllables per word
            for token in token_list:
                word = token.text.lower()
                vowels = "aeiouy"
                # if word starts with a vowel,
                if word[0] in vowels:
                    self.total_number_of_syllables_ += 1
                for index in range(1, len(word)):
                    # if a character is vowel and the preceding character is not,
                    if word[index] in vowels and word[index - 1] not in vowels:
                        self.total_number_of_syllables_ += 1
                # if word ends with e,
                if word.endswith("e"):
                    self.total_number_of_syllables_ -= 1
                # if count was 0,
                if self.total_number_of_syllables_ == 0:
                    self.total_number_of_syllables_ += 1
        return self.total_number_of_syllables_

    def total_number_of_words_more_than_two_syllables(self) -> int:
        """
        returns the number of words more than two syllables
        """
        try:
            return self.total_number_of_words_more_than_two_syllables_
        except AttributeError:
            self.total_number_of_words_more_than_two_syllables_ = 0
            # always remove punctuations
            token_list = [token for token in SE.doc if token.is_punct != True]
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            # start counting syllables per word
            for token in token_list:
                word = token.text.lower()
                total_number_of_syllables_this_word_ = 0
                vowels = "aeiouy"
                # if word starts with a vowel,
                if word[0] in vowels:
                    total_number_of_syllables_this_word_ += 1
                for index in range(1, len(word)):
                    # if a character is vowel and the preceding character is not,
                    if word[index] in vowels and word[index - 1] not in vowels:
                        total_number_of_syllables_this_word_ += 1
                # if word ends with e,
                if word.endswith("e"):
                    total_number_of_syllables_this_word_ -= 1
                # if count was 0,
                if total_number_of_syllables_this_word_ == 0:
                    total_number_of_syllables_this_word_ += 1
                if total_number_of_syllables_this_word_ >= 3:
                    self.total_number_of_words_more_than_two_syllables_ += 1
        return self.total_number_of_words_more_than_two_syllables_

    def total_number_of_words_more_than_three_syllables(self) -> int:
        """
        returns the number of words more than three syllables
        """
        try:
            return self.total_number_of_words_more_than_three_syllables_
        except AttributeError:
            self.total_number_of_words_more_than_three_syllables_ = 0
            # always remove punctuations
            token_list = [token for token in SE.doc if token.is_punct != True]
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            # start counting syllables per word
            for token in token_list:
                word = token.text.lower()
                total_number_of_syllables_this_word_ = 0
                vowels = "aeiouy"
                # if word starts with a vowel,
                if word[0] in vowels:
                    total_number_of_syllables_this_word_ += 1
                for index in range(1, len(word)):
                    # if a character is vowel and the preceding character is not,
                    if word[index] in vowels and word[index - 1] not in vowels:
                        total_number_of_syllables_this_word_ += 1
                # if word ends with e,
                if word.endswith("e"):
                    total_number_of_syllables_this_word_ -= 1
                # if count was 0,
                if total_number_of_syllables_this_word_ == 0:
                    total_number_of_syllables_this_word_ += 1
                if total_number_of_syllables_this_word_ >= 4:
                    self.total_number_of_words_more_than_three_syllables_ += 1
        return self.total_number_of_words_more_than_three_syllables_

    def total_number_of_unique_words(self) -> int:
        """
        returns the number of unique lemmatized words
        """
        try:
            return self.total_number_of_unique_words_
        except AttributeError:   
            token_list = list(self.doc)
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not self.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Count unique tokens in terms of lemma
            unique_token_list = [token.lemma_ for token in SE.doc]
            unique_token_list = list(set(unique_token_list))
            # Calculate and save result
            self.total_number_of_unique_words_ = len(unique_token_list)
            return self.total_number_of_unique_words_
    
    def total_number_of_unique_words_no_lemma(self) -> int:
        """
        returns the number of unique words
        """
        try:
            return self.total_number_of_unique_words_no_lemma_
        except AttributeError:   
            token_list = list(self.doc)
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not self.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Count unique tokens in terms of lemma
            unique_token_list = [token.lemma_ for token in SE.doc]
            unique_token_list = list(set(unique_token_list))
            # Calculate and save result
            self.total_number_of_unique_words_no_lemma_ = len(unique_token_list)
            return self.total_number_of_unique_words_no_lemma_

    def total_number_of_sentences(self) -> int:
        """
        returns the total number of sentences
        """
        try:
            return self.total_number_of_sentences_
        except AttributeError:
            # Calculate and save result
            self.total_number_of_sentences_ = len(list(self.doc.sents))
            return self.total_number_of_sentences_
    
    def total_number_of_characters(self) -> int:
        """
        returns the total number of characters
        """
        try:
            return self.total_number_of_characters_
        except AttributeError:
            token_list = list(self.doc)
            if not self.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not self.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Calculate and save result
            self.total_number_of_characters_ = sum(len(token) for token in token_list)
            return self.total_number_of_characters_
