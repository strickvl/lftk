class PartOfSpeech:
    """PartOfSpeech

    Parent class for features that are in the 'partofspeech' family.
    """
    
    def total_number_of_adjectives(self) -> float:
        """
        returns the number of adjectives
        """
        try: 
            return self.total_number_of_adjectives_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_adjectives_ = pos_list.count("ADJ")
            return self.total_number_of_adjectives_

    def total_number_of_unique_adjectives(self) -> float:
        """
        returns the number of unique adjectives
        """
        try: 
            return self.total_number_of_unique_adjectives_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="ADJ"]
            self.total_number_of_unique_adjectives_ = len([*set(pos_list)])
            return self.total_number_of_unique_adjectives_

    def total_number_of_adpositions(self) -> float:
        """
        returns the number of adpositions
        """
        try: 
            return self.total_number_of_adpositions_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_adpositions_ = pos_list.count("ADP")
            return self.total_number_of_adpositions_
        
    def total_number_of_unique_adpositions(self) -> float:
        """
        returns the number of unique adpositions
        """
        try: 
            return self.total_number_of_unique_adpositions_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="ADP"]
            self.total_number_of_unique_adpositions_ = len([*set(pos_list)])
            return self.total_number_of_unique_adpositions_

    def total_number_of_adverbs(self) -> float:
        """
        returns the number of adverbs
        """
        try: 
            return self.total_number_of_adverbs_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_adverbs_ = pos_list.count("ADV")
            return self.total_number_of_adverbs_
        
    def total_number_of_unique_adverbs(self) -> float:
        """
        returns the number of unique adverbs
        """
        try: 
            return self.total_number_of_unique_adverbs_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="ADV"]
            self.total_number_of_unique_adverbs_ = len([*set(pos_list)])
            return self.total_number_of_unique_adverbs_

    def total_number_of_auxiliaries(self) -> float:
        """
        returns the number of auxiliaries
        """
        try: 
            return self.total_number_of_auxiliaries_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_auxiliaries_ = pos_list.count("AUX")
            return self.total_number_of_auxiliaries_
        
    def total_number_of_unique_auxiliaries(self) -> float:
        """
        returns the number of unique auxiliaries
        """
        try: 
            return self.total_number_of_unique_auxiliaries_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="AUX"]
            self.total_number_of_unique_auxiliaries_ = len([*set(pos_list)])
            return self.total_number_of_unique_auxiliaries_

    def total_number_of_coordinating_conjunctions(self) -> float:
        """
        returns the number of coordinating_conjunctions
        """
        try: 
            return self.total_number_of_coordinating_conjunctions_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_coordinating_conjunctions_ = pos_list.count("CCONJ")
            return self.total_number_of_coordinating_conjunctions_

    def total_number_of_unique_coordinating_conjunctions(self) -> float:
        """
        returns the number of unique coordinating_conjunctions
        """
        try: 
            return self.total_number_of_unique_coordinating_conjunctions_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="CCONJ"]
            self.total_number_of_unique_coordinating_conjunctions_ = len([*set(pos_list)])
            return self.total_number_of_unique_coordinating_conjunctions_

    def total_number_of_determiners(self) -> float:
        """
        returns the number of determiners
        """
        try: 
            return self.total_number_of_determiners_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_determiners_ = pos_list.count("DET")
            return self.total_number_of_determiners_

    def total_number_of_unique_determiners(self) -> float:
        """
        returns the number of unique determiners
        """
        try: 
            return self.total_number_of_unique_determiners_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="DET"]
            self.total_number_of_unique_determiners_ = len([*set(pos_list)])
            return self.total_number_of_unique_determiners_

    def total_number_of_interjections(self) -> float:
        """
        returns the number of interjections
        """
        try: 
            return self.total_number_of_interjections_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_interjections_ = pos_list.count("INTJ")
            return self.total_number_of_interjections_

    def total_number_of_unique_interjections(self) -> float:
        """
        returns the number of unique interjections
        """
        try: 
            return self.total_number_of_unique_interjections_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="INTJ"]
            self.total_number_of_unique_interjections_ = len([*set(pos_list)])
            return self.total_number_of_unique_interjections_

    def total_number_of_nouns(self) -> float:
        """
        returns the number of nouns
        """
        try: 
            return self.total_number_of_nouns_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_nouns_ = pos_list.count("NOUN")
            return self.total_number_of_nouns_

    def total_number_of_unique_nouns(self) -> float:
        """
        returns the number of unique nouns
        """
        try: 
            return self.total_number_of_unique_nouns_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="NOUN"]
            self.total_number_of_unique_nouns_ = len([*set(pos_list)])
            return self.total_number_of_unique_nouns_

    def total_number_of_numerals(self) -> float:
        """
        returns the number of numerals
        """
        try: 
            return self.total_number_of_numerals_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_numerals_ = pos_list.count("NUM")
            return self.total_number_of_numerals_

    def total_number_of_unique_numerals(self) -> float:
        """
        returns the number of unique numerals
        """
        try: 
            return self.total_number_of_unique_numerals_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="NUM"]
            self.total_number_of_unique_numerals_ = len([*set(pos_list)])
            return self.total_number_of_unique_numerals_

    def total_number_of_particles(self) -> float:
        """
        returns the number of particles
        """
        try: 
            return self.total_number_of_particles_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_particles_ = pos_list.count("PART")
            return self.total_number_of_particles_

    def total_number_of_unique_particles(self) -> float:
        """
        returns the number of unique particles
        """
        try: 
            return self.total_number_of_unique_particles_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PART"]
            self.total_number_of_unique_particles_ = len([*set(pos_list)])
            return self.total_number_of_unique_particles_

    def total_number_of_pronouns(self) -> float:
        """
        returns the number of pronouns
        """
        try: 
            return self.total_number_of_pronouns_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_pronouns_ = pos_list.count("PRON")
            return self.total_number_of_pronouns_

    def total_number_of_unique_pronouns(self) -> float:
        """
        returns the number of unique pronouns
        """
        try: 
            return self.total_number_of_unique_pronouns_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PRON"]
            self.total_number_of_unique_pronouns_ = len([*set(pos_list)])
            return self.total_number_of_unique_pronouns_

    def total_number_of_proper_nouns(self) -> float:
        """
        returns the number of proper nouns
        """
        try: 
            return self.total_number_of_proper_nouns_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_proper_nouns_ = pos_list.count("PROPN")
            return self.total_number_of_proper_nouns_

    def total_number_of_unique_proper_nouns(self) -> float:
        """
        returns the number of unique proper nouns
        """
        try: 
            return self.total_number_of_unique_proper_nouns_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PROPN"]
            self.total_number_of_unique_proper_nouns_ = len([*set(pos_list)])
            return self.total_number_of_unique_proper_nouns_

    def total_number_of_punctuations(self) -> float:
        """
        returns the number of punctuations
        """
        try: 
            return self.total_number_of_punctuations_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_punctuations_ = pos_list.count("PUNCT")
            return self.total_number_of_punctuations_

    def total_number_of_unique_punctuations(self) -> float:
        """
        returns the number of unique punctuations
        """
        try: 
            return self.total_number_of_unique_punctuations_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PUNCT"]
            self.total_number_of_unique_punctuations_ = len([*set(pos_list)])
            return self.total_number_of_unique_punctuations_

    def total_number_of_subordinating_conjunctions(self) -> float:
        """
        returns the number of subordinating conjunctions
        """
        try: 
            return self.total_number_of_subordinating_conjunctions_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_subordinating_conjunctions_ = pos_list.count("SCONJ")
            return self.total_number_of_subordinating_conjunctions_

    def total_number_of_unique_subordinating_conjunctions(self) -> float:
        """
        returns the number of unique subordinating conjunctions
        """
        try: 
            return self.total_number_of_unique_subordinating_conjunctions_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="SCONJ"]
            self.total_number_of_unique_subordinating_conjunctions_ = len([*set(pos_list)])
            return self.total_number_of_unique_subordinating_conjunctions_

    def total_number_of_symbols(self) -> float:
        """
        returns the number of symbols
        """
        try: 
            return self.total_number_of_symbols_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_symbols_ = pos_list.count("SYM")
            return self.total_number_of_symbols_

    def total_number_of_unique_symbols(self) -> float:
        """
        returns the number of unique symbols
        """
        try: 
            return self.total_number_of_unique_symbols_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="SYM"]
            self.total_number_of_unique_symbols_ = len([*set(pos_list)])
            return self.total_number_of_unique_symbols_

    def total_number_of_verbs(self) -> float:
        """
        returns the number of verbs
        """
        try: 
            return self.total_number_of_verbs_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_verbs_ = pos_list.count("VERB")
            return self.total_number_of_verbs_
    
    def total_number_of_unique_verbs(self) -> float:
        """
        returns the number of unique verbs
        """
        try: 
            return self.total_number_of_unique_verbs_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="VERB"]
            self.total_number_of_unique_verbs_ = len([*set(pos_list)])
            return self.total_number_of_unique_verbs_

    def total_number_of_spaces(self) -> float:
        """
        returns the number of spaces
        """
        try: 
            return self.total_number_of_spaces_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            self.total_number_of_spaces_ = pos_list.count("SPACE")
            return self.total_number_of_spaces_

    def total_number_of_unique_spaces(self) -> float:
        """
        returns the number of unique spaces
        """
        try: 
            return self.total_number_of_unique_spaces_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="SPACE"]
            self.total_number_of_unique_spaces_ = len([*set(pos_list)])
            return self.total_number_of_unique_spaces_
