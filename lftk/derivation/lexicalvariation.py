import math

from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class LexicalVariation(FoundationCollector):
    """LexicalVariation

    Parent class for features that are in the 'lexicalvariation' family.
    """

    def simple_adjectives_variation(self) -> float:
        """
        returns value of (total number of unique adjectives / total number of adjectives)
        """
        try:
            return self.simple_adjectives_variation_
        except AttributeError:
            total_number_of_unique_adjectives_ = (
                FoundationCollector.total_number_of_unique_adjectives(self)
            )
            total_number_of_adjectives_ = (
                FoundationCollector.total_number_of_adjectives(self)
            )
            self.simple_adjectives_variation_ = safe_division(
                total_number_of_unique_adjectives_, total_number_of_adjectives_
            )
            return self.simple_adjectives_variation_
    
    def root_adjectives_variation(self) -> float:
        """
        returns value of (total number of unique adjectives / root(total number of adjectives))
        """
        try:
            return self.root_adjectives_variation_
        except AttributeError:
            total_number_of_unique_adjectives_ = (
                FoundationCollector.total_number_of_unique_adjectives(self)
            )
            total_number_of_adjectives_ = (
                FoundationCollector.total_number_of_adjectives(self)
            )
            self.root_adjectives_variation_ = safe_division(
                total_number_of_unique_adjectives_,
                math.sqrt(total_number_of_adjectives_),
            )
            return self.root_adjectives_variation_
        
    def corrected_adjectives_variation(self) -> float:
        """
        returns value of (total number of unique adjectives / root(2*total number of adjectives))
        """
        try:
            return self.corrected_adjectives_variation_
        except AttributeError:
            total_number_of_unique_adjectives_ = (
                FoundationCollector.total_number_of_unique_adjectives(self)
            )
            total_number_of_adjectives_ = (
                FoundationCollector.total_number_of_adjectives(self)
            )
            self.corrected_adjectives_variation_ = safe_division(
                total_number_of_unique_adjectives_,
                math.sqrt(2 * total_number_of_adjectives_),
            )
            return self.corrected_adjectives_variation_
    
    def simple_adpositions_variation(self) -> float:
        """
        returns value of (total number of unique adpositions / total number of adpositions)
        """
        try:
            return self.simple_adpositions_variation_
        except AttributeError:
            total_number_of_unique_adpositions_ = (
                FoundationCollector.total_number_of_unique_adpositions(self)
            )
            total_number_of_adpositions_ = (
                FoundationCollector.total_number_of_adpositions(self)
            )
            self.simple_adpositions_variation_ = safe_division(
                total_number_of_unique_adpositions_, total_number_of_adpositions_
            )
            return self.simple_adpositions_variation_
    
    def root_adpositions_variation(self) -> float:
        """
        returns value of (total number of unique adpositions / root(total number of adpositions))
        """
        try:
            return self.root_adpositions_variation_
        except AttributeError:
            total_number_of_unique_adpositions_ = (
                FoundationCollector.total_number_of_unique_adpositions(self)
            )
            total_number_of_adpositions_ = (
                FoundationCollector.total_number_of_adpositions(self)
            )
            self.root_adpositions_variation_ = safe_division(
                total_number_of_unique_adpositions_,
                math.sqrt(total_number_of_adpositions_),
            )
            return self.root_adpositions_variation_
        
    def corrected_adpositions_variation(self) -> float:
        """
        returns value of (total number of unique adpositions / root(2*total number of adpositions))
        """
        try:
            return self.corrected_adpositions_variation_
        except AttributeError:
            total_number_of_unique_adpositions_ = (
                FoundationCollector.total_number_of_unique_adpositions(self)
            )
            total_number_of_adpositions_ = (
                FoundationCollector.total_number_of_adpositions(self)
            )
            self.corrected_adpositions_variation_ = safe_division(
                total_number_of_unique_adpositions_,
                math.sqrt(2 * total_number_of_adpositions_),
            )
            return self.corrected_adpositions_variation_
    
    def simple_adverbs_variation(self) -> float:
        """
        returns value of (total number of unique adverbs / total number of adverbs)
        """
        try:
            return self.simple_adverbs_variation_
        except AttributeError:
            total_number_of_unique_adverbs_ = (
                FoundationCollector.total_number_of_unique_adverbs(self)
            )
            total_number_of_adverbs_ = FoundationCollector.total_number_of_adverbs(self)
            self.simple_adverbs_variation_ = safe_division(
                total_number_of_unique_adverbs_, total_number_of_adverbs_
            )
            return self.simple_adverbs_variation_
    
    def root_adverbs_variation(self) -> float:
        """
        returns value of (total number of unique adverbs / root(total number of adverbs))
        """
        try:
            return self.root_adverbs_variation_
        except AttributeError:
            total_number_of_unique_adverbs_ = (
                FoundationCollector.total_number_of_unique_adverbs(self)
            )
            total_number_of_adverbs_ = FoundationCollector.total_number_of_adverbs(self)
            self.root_adverbs_variation_ = safe_division(
                total_number_of_unique_adverbs_,
                math.sqrt(total_number_of_adverbs_),
            )
            return self.root_adverbs_variation_
        
    def corrected_adverbs_variation(self) -> float:
        """
        returns value of (total number of unique adverbs / root(2*total number of adverbs))
        """
        try:
            return self.corrected_adverbs_variation_
        except AttributeError:
            total_number_of_unique_adverbs_ = (
                FoundationCollector.total_number_of_unique_adverbs(self)
            )
            total_number_of_adverbs_ = FoundationCollector.total_number_of_adverbs(self)
            self.corrected_adverbs_variation_ = safe_division(
                total_number_of_unique_adverbs_,
                math.sqrt(2 * total_number_of_adverbs_),
            )
            return self.corrected_adverbs_variation_
    
    def simple_auxiliaries_variation(self) -> float:
        """
        returns value of (total number of unique auxiliaries / total number of auxiliaries)
        """
        try:
            return self.simple_auxiliaries_variation_
        except AttributeError:
            total_number_of_unique_auxiliaries_ = (
                FoundationCollector.total_number_of_unique_auxiliaries(self)
            )
            total_number_of_auxiliaries_ = (
                FoundationCollector.total_number_of_auxiliaries(self)
            )
            self.simple_auxiliaries_variation_ = safe_division(
                total_number_of_unique_auxiliaries_, total_number_of_auxiliaries_
            )
            return self.simple_auxiliaries_variation_
    
    def root_auxiliaries_variation(self) -> float:
        """
        returns value of (total number of unique auxiliaries / root(total number of auxiliaries))
        """
        try:
            return self.root_auxiliaries_variation_
        except AttributeError:
            total_number_of_unique_auxiliaries_ = (
                FoundationCollector.total_number_of_unique_auxiliaries(self)
            )
            total_number_of_auxiliaries_ = (
                FoundationCollector.total_number_of_auxiliaries(self)
            )
            self.root_auxiliaries_variation_ = safe_division(
                total_number_of_unique_auxiliaries_,
                math.sqrt(total_number_of_auxiliaries_),
            )
            return self.root_auxiliaries_variation_
        
    def corrected_auxiliaries_variation(self) -> float:
        """
        returns value of (total number of unique auxiliaries / root(2*total number of auxiliaries))
        """
        try:
            return self.corrected_auxiliaries_variation_
        except AttributeError:
            total_number_of_unique_auxiliaries_ = (
                FoundationCollector.total_number_of_unique_auxiliaries(self)
            )
            total_number_of_auxiliaries_ = (
                FoundationCollector.total_number_of_auxiliaries(self)
            )
            self.corrected_auxiliaries_variation_ = safe_division(
                total_number_of_unique_auxiliaries_,
                math.sqrt(2 * total_number_of_auxiliaries_),
            )
            return self.corrected_auxiliaries_variation_
        
    def simple_coordinating_conjunctions_variation(self) -> float:
        """
        returns value of (total number of unique coordinating conjunctions / total number of coordinating conjunctions)
        """
        try:
            return self.simple_coordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_coordinating_conjunctions_ = FoundationCollector.total_number_of_unique_coordinating_conjunctions(
                self
            )
            total_number_of_coordinating_conjunctions_ = (
                FoundationCollector.total_number_of_coordinating_conjunctions(self)
            )
            self.simple_coordinating_conjunctions_variation_ = safe_division(
                total_number_of_unique_coordinating_conjunctions_,
                total_number_of_coordinating_conjunctions_,
            )
            return self.simple_coordinating_conjunctions_variation_
    
    def root_coordinating_conjunctions_variation(self) -> float:
        """
        returns value of (total number of unique coordinating conjunctions / root(total number of coordinating conjunctions))
        """
        try:
            return self.root_coordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_coordinating_conjunctions_ = FoundationCollector.total_number_of_unique_coordinating_conjunctions(
                self
            )
            total_number_of_coordinating_conjunctions_ = (
                FoundationCollector.total_number_of_coordinating_conjunctions(self)
            )
            self.root_coordinating_conjunctions_variation_ = safe_division(
                total_number_of_unique_coordinating_conjunctions_,
                math.sqrt(total_number_of_coordinating_conjunctions_),
            )
            return self.root_coordinating_conjunctions_variation_
        
    def corrected_coordinating_conjunctions_variation(self) -> float:
        """
        returns value of (total number of unique coordinating conjunctions / root(2*total number of coordinating conjunctions))
        """
        try:
            return self.corrected_coordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_coordinating_conjunctions_ = FoundationCollector.total_number_of_unique_coordinating_conjunctions(
                self
            )
            total_number_of_coordinating_conjunctions_ = (
                FoundationCollector.total_number_of_coordinating_conjunctions(self)
            )
            self.corrected_coordinating_conjunctions_variation_ = safe_division(
                total_number_of_unique_coordinating_conjunctions_,
                math.sqrt(2 * total_number_of_coordinating_conjunctions_),
            )
            return self.corrected_coordinating_conjunctions_variation_
    
    def simple_determiners_variation(self) -> float:
        """
        returns value of (total number of unique determiners / total number of determiners)
        """
        try:
            return self.simple_determiners_variation_
        except AttributeError:
            total_number_of_unique_determiners_ = (
                FoundationCollector.total_number_of_unique_determiners(self)
            )
            total_number_of_determiners_ = (
                FoundationCollector.total_number_of_determiners(self)
            )
            self.simple_determiners_variation_ = safe_division(
                total_number_of_unique_determiners_, total_number_of_determiners_
            )
            return self.simple_determiners_variation_
    
    def root_determiners_variation(self) -> float:
        """
        returns value of (total number of unique determiners / root(total number of determiners))
        """
        try:
            return self.root_determiners_variation_
        except AttributeError:
            total_number_of_unique_determiners_ = (
                FoundationCollector.total_number_of_unique_determiners(self)
            )
            total_number_of_determiners_ = (
                FoundationCollector.total_number_of_determiners(self)
            )
            self.root_determiners_variation_ = safe_division(
                total_number_of_unique_determiners_,
                math.sqrt(total_number_of_determiners_),
            )
            return self.root_determiners_variation_
        
    def corrected_determiners_variation(self) -> float:
        """
        returns value of (total number of unique determiners / root(2*total number of determiners))
        """
        try:
            return self.corrected_determiners_variation_
        except AttributeError:
            total_number_of_unique_determiners_ = (
                FoundationCollector.total_number_of_unique_determiners(self)
            )
            total_number_of_determiners_ = (
                FoundationCollector.total_number_of_determiners(self)
            )
            self.corrected_determiners_variation_ = safe_division(
                total_number_of_unique_determiners_,
                math.sqrt(2 * total_number_of_determiners_),
            )
            return self.corrected_determiners_variation_
    
    def simple_interjections_variation(self) -> float:
        """
        returns value of (total number of unique interjections / total number of interjections)
        """
        try:
            return self.simple_interjections_variation_
        except AttributeError:
            total_number_of_unique_interjections_ = (
                FoundationCollector.total_number_of_unique_interjections(self)
            )
            total_number_of_interjections_ = (
                FoundationCollector.total_number_of_interjections(self)
            )
            self.simple_interjections_variation_ = safe_division(
                total_number_of_unique_interjections_,
                total_number_of_interjections_,
            )
            return self.simple_interjections_variation_
    
    def root_interjections_variation(self) -> float:
        """
        returns value of (total number of unique interjections / root(total number of interjections))
        """
        try:
            return self.root_interjections_variation_
        except AttributeError:
            total_number_of_unique_interjections_ = (
                FoundationCollector.total_number_of_unique_interjections(self)
            )
            total_number_of_interjections_ = (
                FoundationCollector.total_number_of_interjections(self)
            )
            self.root_interjections_variation_ = safe_division(
                total_number_of_unique_interjections_,
                math.sqrt(total_number_of_interjections_),
            )
            return self.root_interjections_variation_
        
    def corrected_interjections_variation(self) -> float:
        """
        returns value of (total number of unique interjections / root(2*total number of interjections))
        """
        try:
            return self.corrected_interjections_variation_
        except AttributeError:
            total_number_of_unique_interjections_ = (
                FoundationCollector.total_number_of_unique_interjections(self)
            )
            total_number_of_interjections_ = (
                FoundationCollector.total_number_of_interjections(self)
            )
            self.corrected_interjections_variation_ = safe_division(
                total_number_of_unique_interjections_,
                math.sqrt(2 * total_number_of_interjections_),
            )
            return self.corrected_interjections_variation_
    
    def simple_nouns_variation(self) -> float:
        """
        returns value of (total number of unique nouns / total number of nouns)
        """
        try:
            return self.simple_nouns_variation_
        except AttributeError:
            total_number_of_unique_nouns_ = (
                FoundationCollector.total_number_of_unique_nouns(self)
            )
            total_number_of_nouns_ = FoundationCollector.total_number_of_nouns(self)
            self.simple_nouns_variation_ = safe_division(
                total_number_of_unique_nouns_, total_number_of_nouns_
            )
            return self.simple_nouns_variation_
    
    def root_nouns_variation(self) -> float:
        """
        returns value of (total number of unique nouns / root(total number of nouns))
        """
        try:
            return self.root_nouns_variation_
        except AttributeError:
            total_number_of_unique_nouns_ = (
                FoundationCollector.total_number_of_unique_nouns(self)
            )
            total_number_of_nouns_ = FoundationCollector.total_number_of_nouns(self)
            self.root_nouns_variation_ = safe_division(
                total_number_of_unique_nouns_, math.sqrt(total_number_of_nouns_)
            )
            return self.root_nouns_variation_
        
    def corrected_nouns_variation(self) -> float:
        """
        returns value of (total number of unique nouns / root(2*total number of nouns))
        """
        try:
            return self.corrected_nouns_variation_
        except AttributeError:
            total_number_of_unique_nouns_ = (
                FoundationCollector.total_number_of_unique_nouns(self)
            )
            total_number_of_nouns_ = FoundationCollector.total_number_of_nouns(self)
            self.corrected_nouns_variation_ = safe_division(
                total_number_of_unique_nouns_,
                math.sqrt(2 * total_number_of_nouns_),
            )
            return self.corrected_nouns_variation_
    
    def simple_numerals_variation(self) -> float:
        """
        returns value of (total number of unique numerals / total number of numerals)
        """
        try:
            return self.simple_numerals_variation_
        except AttributeError:
            total_number_of_unique_numerals_ = (
                FoundationCollector.total_number_of_unique_numerals(self)
            )
            total_number_of_numerals_ = FoundationCollector.total_number_of_numerals(self)
            self.simple_numerals_variation_ = safe_division(
                total_number_of_unique_numerals_, total_number_of_numerals_
            )
            return self.simple_numerals_variation_
    
    def root_numerals_variation(self) -> float:
        """
        returns value of (total number of unique numerals / root(total number of numerals))
        """
        try:
            return self.root_numerals_variation_
        except AttributeError:
            total_number_of_unique_numerals_ = (
                FoundationCollector.total_number_of_unique_numerals(self)
            )
            total_number_of_numerals_ = FoundationCollector.total_number_of_numerals(self)
            self.root_numerals_variation_ = safe_division(
                total_number_of_unique_numerals_,
                math.sqrt(total_number_of_numerals_),
            )
            return self.root_numerals_variation_
        
    def corrected_numerals_variation(self) -> float:
        """
        returns value of (total number of unique numerals / root(2*total number of numerals))
        """
        try:
            return self.corrected_numerals_variation_
        except AttributeError:
            total_number_of_unique_numerals_ = (
                FoundationCollector.total_number_of_unique_numerals(self)
            )
            total_number_of_numerals_ = FoundationCollector.total_number_of_numerals(self)
            self.corrected_numerals_variation_ = safe_division(
                total_number_of_unique_numerals_,
                math.sqrt(2 * total_number_of_numerals_),
            )
            return self.corrected_numerals_variation_
    
    def simple_particles_variation(self) -> float:
        """
        returns value of (total number of unique particles / total number of particles)
        """
        try:
            return self.simple_particles_variation_
        except AttributeError:
            total_number_of_unique_particles_ = (
                FoundationCollector.total_number_of_unique_particles(self)
            )
            total_number_of_particles_ = (
                FoundationCollector.total_number_of_particles(self)
            )
            self.simple_particles_variation_ = safe_division(
                total_number_of_unique_particles_, total_number_of_particles_
            )
            return self.simple_particles_variation_
    
    def root_particles_variation(self) -> float:
        """
        returns value of (total number of unique particles / root(total number of particles))
        """
        try:
            return self.root_particles_variation_
        except AttributeError:
            total_number_of_unique_particles_ = (
                FoundationCollector.total_number_of_unique_particles(self)
            )
            total_number_of_particles_ = (
                FoundationCollector.total_number_of_particles(self)
            )
            self.root_particles_variation_ = safe_division(
                total_number_of_unique_particles_,
                math.sqrt(total_number_of_particles_),
            )
            return self.root_particles_variation_
        
    def corrected_particles_variation(self) -> float:
        """
        returns value of (total number of unique particles / root(2*total number of particles))
        """
        try:
            return self.corrected_particles_variation_
        except AttributeError:
            total_number_of_unique_particles_ = (
                FoundationCollector.total_number_of_unique_particles(self)
            )
            total_number_of_particles_ = (
                FoundationCollector.total_number_of_particles(self)
            )
            self.corrected_particles_variation_ = safe_division(
                total_number_of_unique_particles_,
                math.sqrt(2 * total_number_of_particles_),
            )
            return self.corrected_particles_variation_
    
    def simple_pronouns_variation(self) -> float:
        """
        returns value of (total number of unique pronouns / total number of pronouns)
        """
        try:
            return self.simple_pronouns_variation_
        except AttributeError:
            total_number_of_unique_pronouns_ = (
                FoundationCollector.total_number_of_unique_pronouns(self)
            )
            total_number_of_pronouns_ = FoundationCollector.total_number_of_pronouns(self)
            self.simple_pronouns_variation_ = safe_division(
                total_number_of_unique_pronouns_, total_number_of_pronouns_
            )
            return self.simple_pronouns_variation_
    
    def root_pronouns_variation(self) -> float:
        """
        returns value of (total number of unique pronouns / root(total number of pronouns))
        """
        try:
            return self.root_pronouns_variation_
        except AttributeError:
            total_number_of_unique_pronouns_ = (
                FoundationCollector.total_number_of_unique_pronouns(self)
            )
            total_number_of_pronouns_ = FoundationCollector.total_number_of_pronouns(self)
            self.root_pronouns_variation_ = safe_division(
                total_number_of_unique_pronouns_,
                math.sqrt(total_number_of_pronouns_),
            )
            return self.root_pronouns_variation_
        
    def corrected_pronouns_variation(self) -> float:
        """
        returns value of (total number of unique pronouns / root(2*total number of pronouns))
        """
        try:
            return self.corrected_pronouns_variation_
        except AttributeError:
            total_number_of_unique_pronouns_ = (
                FoundationCollector.total_number_of_unique_pronouns(self)
            )
            total_number_of_pronouns_ = FoundationCollector.total_number_of_pronouns(self)
            self.corrected_pronouns_variation_ = safe_division(
                total_number_of_unique_pronouns_,
                math.sqrt(2 * total_number_of_pronouns_),
            )
            return self.corrected_pronouns_variation_
    
    def simple_proper_nouns_variation(self) -> float:
        """
        returns value of (total number of unique proper nouns / total number of proper nouns)
        """
        try:
            return self.simple_proper_nouns_variation_
        except AttributeError:
            total_number_of_unique_proper_nouns_ = (
                FoundationCollector.total_number_of_unique_proper_nouns(self)
            )
            total_number_of_proper_nouns_ = (
                FoundationCollector.total_number_of_proper_nouns(self)
            )
            self.simple_proper_nouns_variation_ = safe_division(
                total_number_of_unique_proper_nouns_, total_number_of_proper_nouns_
            )
            return self.simple_proper_nouns_variation_
    
    def root_proper_nouns_variation(self) -> float:
        """
        returns value of (total number of unique proper nouns / root(total number of proper nouns))
        """
        try:
            return self.root_proper_nouns_variation_
        except AttributeError:
            total_number_of_unique_proper_nouns_ = (
                FoundationCollector.total_number_of_unique_proper_nouns(self)
            )
            total_number_of_proper_nouns_ = (
                FoundationCollector.total_number_of_proper_nouns(self)
            )
            self.root_proper_nouns_variation_ = safe_division(
                total_number_of_unique_proper_nouns_,
                math.sqrt(total_number_of_proper_nouns_),
            )
            return self.root_proper_nouns_variation_
        
    def corrected_proper_nouns_variation(self) -> float:
        """
        returns value of (total number of unique proper nouns / root(2*total number of proper nouns))
        """
        try:
            return self.corrected_proper_nouns_variation_
        except AttributeError:
            total_number_of_unique_proper_nouns_ = (
                FoundationCollector.total_number_of_unique_proper_nouns(self)
            )
            total_number_of_proper_nouns_ = (
                FoundationCollector.total_number_of_proper_nouns(self)
            )
            self.corrected_proper_nouns_variation_ = safe_division(
                total_number_of_unique_proper_nouns_,
                math.sqrt(2 * total_number_of_proper_nouns_),
            )
            return self.corrected_proper_nouns_variation_
    
    def simple_punctuations_variation(self) -> float:
        """
        returns value of (total number of unique punctuations / total number of punctuations)
        """
        try:
            return self.simple_punctuations_variation_
        except AttributeError:
            total_number_of_unique_punctuations_ = (
                FoundationCollector.total_number_of_unique_punctuations(self)
            )
            total_number_of_punctuations_ = (
                FoundationCollector.total_number_of_punctuations(self)
            )
            self.simple_punctuations_variation_ = safe_division(
                total_number_of_unique_punctuations_, total_number_of_punctuations_
            )
            return self.simple_punctuations_variation_
    
    def root_punctuations_variation(self) -> float:
        """
        returns value of (total number of unique punctuations / root(total number of punctuations))
        """
        try:
            return self.root_punctuations_variation_
        except AttributeError:
            total_number_of_unique_punctuations_ = (
                FoundationCollector.total_number_of_unique_punctuations(self)
            )
            total_number_of_punctuations_ = (
                FoundationCollector.total_number_of_punctuations(self)
            )
            self.root_punctuations_variation_ = safe_division(
                total_number_of_unique_punctuations_,
                math.sqrt(total_number_of_punctuations_),
            )
            return self.root_punctuations_variation_
        
    def corrected_punctuations_variation(self) -> float:
        """
        returns value of (total number of unique punctuations / root(2*total number of punctuations))
        """
        try:
            return self.corrected_punctuations_variation_
        except AttributeError:
            total_number_of_unique_punctuations_ = (
                FoundationCollector.total_number_of_unique_punctuations(self)
            )
            total_number_of_punctuations_ = (
                FoundationCollector.total_number_of_punctuations(self)
            )
            self.corrected_punctuations_variation_ = safe_division(
                total_number_of_unique_punctuations_,
                math.sqrt(2 * total_number_of_punctuations_),
            )
            return self.corrected_punctuations_variation_
    
    def simple_subordinating_conjunctions_variation(self) -> float:
        """
        returns value of (total number of unique subordinating conjunctions / total number of subordinating conjunctions)
        """
        try:
            return self.simple_subordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_subordinating_conjunctions_ = FoundationCollector.total_number_of_unique_subordinating_conjunctions(
                self
            )
            total_number_of_subordinating_conjunctions_ = (
                FoundationCollector.total_number_of_subordinating_conjunctions(
                    self
                )
            )
            self.simple_subordinating_conjunctions_variation_ = safe_division(
                total_number_of_unique_subordinating_conjunctions_,
                total_number_of_subordinating_conjunctions_,
            )
            return self.simple_subordinating_conjunctions_variation_
    
    def root_subordinating_conjunctions_variation(self) -> float:
        """
        returns value of (total number of unique subordinating conjunctions / root(total number of subordinating conjunctions))
        """
        try:
            return self.root_subordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_subordinating_conjunctions_ = FoundationCollector.total_number_of_unique_subordinating_conjunctions(
                self
            )
            total_number_of_subordinating_conjunctions_ = (
                FoundationCollector.total_number_of_subordinating_conjunctions(
                    self
                )
            )
            self.root_subordinating_conjunctions_variation_ = safe_division(
                total_number_of_unique_subordinating_conjunctions_,
                math.sqrt(total_number_of_subordinating_conjunctions_),
            )
            return self.root_subordinating_conjunctions_variation_
        
    def corrected_subordinating_conjunctions_variation(self) -> float:
        """
        returns value of (total number of unique subordinating conjunctions / root(2*total number of subordinating conjunctions))
        """
        try:
            return self.corrected_subordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_subordinating_conjunctions_ = FoundationCollector.total_number_of_unique_subordinating_conjunctions(
                self
            )
            total_number_of_subordinating_conjunctions_ = (
                FoundationCollector.total_number_of_subordinating_conjunctions(
                    self
                )
            )
            self.corrected_subordinating_conjunctions_variation_ = safe_division(
                total_number_of_unique_subordinating_conjunctions_,
                math.sqrt(2 * total_number_of_subordinating_conjunctions_),
            )
            return self.corrected_subordinating_conjunctions_variation_
    
    def simple_symbols_variation(self) -> float:
        """
        returns value of (total number of unique symbols / total number of symbols)
        """
        try:
            return self.simple_symbols_variation_
        except AttributeError:
            total_number_of_unique_symbols_ = (
                FoundationCollector.total_number_of_unique_symbols(self)
            )
            total_number_of_symbols_ = FoundationCollector.total_number_of_symbols(self)
            self.simple_symbols_variation_ = safe_division(
                total_number_of_unique_symbols_, total_number_of_symbols_
            )
            return self.simple_symbols_variation_
    
    def root_symbols_variation(self) -> float:
        """
        returns value of (total number of unique symbols / root(total number of symbols))
        """
        try:
            return self.root_symbols_variation_
        except AttributeError:
            total_number_of_unique_symbols_ = (
                FoundationCollector.total_number_of_unique_symbols(self)
            )
            total_number_of_symbols_ = FoundationCollector.total_number_of_symbols(self)
            self.root_symbols_variation_ = safe_division(
                total_number_of_unique_symbols_,
                math.sqrt(total_number_of_symbols_),
            )
            return self.root_symbols_variation_
        
    def corrected_symbols_variation(self) -> float:
        """
        returns value of (total number of unique symbols / root(2*total number of symbols))
        """
        try:
            return self.corrected_symbols_variation_
        except AttributeError:
            total_number_of_unique_symbols_ = (
                FoundationCollector.total_number_of_unique_symbols(self)
            )
            total_number_of_symbols_ = FoundationCollector.total_number_of_symbols(self)
            self.corrected_symbols_variation_ = safe_division(
                total_number_of_unique_symbols_,
                math.sqrt(2 * total_number_of_symbols_),
            )
            return self.corrected_symbols_variation_
    
    def simple_verbs_variation(self) -> float:
        """
        returns value of (total number of unique verbs / total number of verbs)
        """
        try:
            return self.simple_verbs_variation_
        except AttributeError:
            total_number_of_unique_verbs_ = (
                FoundationCollector.total_number_of_unique_verbs(self)
            )
            total_number_of_verbs_ = FoundationCollector.total_number_of_verbs(self)
            self.simple_verbs_variation_ = safe_division(
                total_number_of_unique_verbs_, total_number_of_verbs_
            )
            return self.simple_verbs_variation_
    
    def root_verbs_variation(self) -> float:
        """
        returns value of (total number of unique verbs / root(total number of verbs))
        """
        try:
            return self.root_verbs_variation_
        except AttributeError:
            total_number_of_unique_verbs_ = (
                FoundationCollector.total_number_of_unique_verbs(self)
            )
            total_number_of_verbs_ = FoundationCollector.total_number_of_verbs(self)
            self.root_verbs_variation_ = safe_division(
                total_number_of_unique_verbs_, math.sqrt(total_number_of_verbs_)
            )
            return self.root_verbs_variation_
        
    def corrected_verbs_variation(self) -> float:
        """
        returns value of (total number of unique verbs / root(2*total number of verbs))
        """
        try:
            return self.corrected_verbs_variation_
        except AttributeError:
            total_number_of_unique_verbs_ = (
                FoundationCollector.total_number_of_unique_verbs(self)
            )
            total_number_of_verbs_ = FoundationCollector.total_number_of_verbs(self)
            self.corrected_verbs_variation_ = safe_division(
                total_number_of_unique_verbs_,
                math.sqrt(2 * total_number_of_verbs_),
            )
            return self.corrected_verbs_variation_
        
    def simple_spaces_variation(self) -> float:
        """
        returns value of (total number of unique spaces / total number of spaces)
        """
        try:
            return self.simple_spaces_variation_
        except AttributeError:
            total_number_of_unique_spaces_ = (
                FoundationCollector.total_number_of_unique_spaces(self)
            )
            total_number_of_spaces_ = FoundationCollector.total_number_of_spaces(self)
            self.simple_spaces_variation_ = safe_division(
                total_number_of_unique_spaces_, total_number_of_spaces_
            )
            return self.simple_spaces_variation_
    
    def root_spaces_variation(self) -> float:
        """
        returns value of (total number of unique spaces / root(total number of spaces))
        """
        try:
            return self.root_spaces_variation_
        except AttributeError:
            total_number_of_unique_spaces_ = (
                FoundationCollector.total_number_of_unique_spaces(self)
            )
            total_number_of_spaces_ = FoundationCollector.total_number_of_spaces(self)
            self.root_spaces_variation_ = safe_division(
                total_number_of_unique_spaces_, math.sqrt(total_number_of_spaces_)
            )
            return self.root_spaces_variation_
        
    def corrected_spaces_variation(self) -> float:
        """
        returns value of (total number of unique spaces / root(2*total number of spaces))
        """
        try:
            return self.corrected_spaces_variation_
        except AttributeError:
            total_number_of_unique_spaces_ = (
                FoundationCollector.total_number_of_unique_spaces(self)
            )
            total_number_of_spaces_ = FoundationCollector.total_number_of_spaces(self)
            self.corrected_spaces_variation_ = safe_division(
                total_number_of_unique_spaces_,
                math.sqrt(2 * total_number_of_spaces_),
            )
            return self.corrected_spaces_variation_