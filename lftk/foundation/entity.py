class Entity:
    """Entity

    Parent class for features that are in the 'entity' family.
    """

    def total_number_of_named_entities(self) -> int:
        """
        returns the number of named entities
        """
        try:
            return self.total_number_of_named_entities_
        except AttributeError:
            doc_total = sum(1 for _ in self.doc.ents)
            self.total_number_of_named_entities_ = doc_total
            return self.total_number_of_named_entities_
   
    def total_number_of_named_entities_person(self) -> int:
        """
        returns the number of named entities that are PERSON (People, including fictional)
        """
        try:
            return self.total_number_of_named_entities_person_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "PERSON")
            self.total_number_of_named_entities_person_ = doc_total
            return self.total_number_of_named_entities_person_
        
    def total_number_of_named_entities_norp(self) -> int:
        """
        returns the number of named entities that are NORP (Nationalities or religious or political groups)
        """
        try:
            return self.total_number_of_named_entities_norp_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "NORP")
            self.total_number_of_named_entities_norp_ = doc_total
            return self.total_number_of_named_entities_norp_

    def total_number_of_named_entities_fac(self) -> int:
        """
        returns the number of named entities that are FAC (Buildings, airports, highways, bridges, etc.)
        """
        try:
            return self.total_number_of_named_entities_fac_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "FAC")
            self.total_number_of_named_entities_fac_ = doc_total
            return self.total_number_of_named_entities_fac_

    def total_number_of_named_entities_org(self) -> int:
        """
        returns the number of named entities that are ORG (Companies, agencies, institutions, etc.)
        """
        try:
            return self.total_number_of_named_entities_org_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "ORG")
            self.total_number_of_named_entities_org_ = doc_total
            return self.total_number_of_named_entities_org_
    
    def total_number_of_named_entities_gpe(self) -> int:
        """
        returns the number of named entities that are GPE (Countries, cities, states.)
        """
        try:
            return self.total_number_of_named_entities_gpe_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "GPE")
            self.total_number_of_named_entities_gpe_ = doc_total
            return self.total_number_of_named_entities_gpe_
    
    def total_number_of_named_entities_loc(self) -> int:
        """
        returns the number of named entities that are LOC (Non-GPE locations, mountain ranges, bodies of water.)
        """
        try:
            return self.total_number_of_named_entities_loc_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "LOC")
            self.total_number_of_named_entities_loc_ = doc_total
            return self.total_number_of_named_entities_loc_
    
    def total_number_of_named_entities_product(self) -> int:
        """
        returns the number of named entities that are PRODUCT (Objects, vehicles, foods, etc. (Not services.)
        """
        try:
            return self.total_number_of_named_entities_product_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "PRODUCT")
            self.total_number_of_named_entities_product_ = doc_total
            return self.total_number_of_named_entities_product_
    
    def total_number_of_named_entities_event(self) -> int:
        """
        returns the number of named entities that are EVENT (Named hurricanes, battles, wars, sports events, etc.)
        """
        try:
            return self.total_number_of_named_entities_event_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "EVENT")
            self.total_number_of_named_entities_event_ = doc_total
            return self.total_number_of_named_entities_event_
    
    def total_number_of_named_entities_art(self) -> int:
        """
        returns the number of named entities that are WORK_OF_ART (Titles of books, songs, etc.)
        """
        try:
            return self.total_number_of_named_entities_art_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "WORK_OF_ART")
            self.total_number_of_named_entities_art_ = doc_total
            return self.total_number_of_named_entities_art_
    
    def total_number_of_named_entities_law(self) -> int:
        """
        returns the number of named entities that are LAW (Named documents made into laws.)
        """
        try:
            return self.total_number_of_named_entities_law_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "LAW")
            self.total_number_of_named_entities_law_ = doc_total
            return self.total_number_of_named_entities_law_
    
    def total_number_of_named_entities_language(self) -> int:
        """
        returns the number of named entities that are LANGUAGE (Any named language.)
        """
        try:
            return self.total_number_of_named_entities_language_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "LANGUAGE")
            self.total_number_of_named_entities_language_ = doc_total
            return self.total_number_of_named_entities_language_
    
    def total_number_of_named_entities_date(self) -> int:
        """
        returns the number of named entities that are DATE (Absolute or relative dates or periods.)
        """
        try:
            return self.total_number_of_named_entities_date_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "DATE")
            self.total_number_of_named_entities_date_ = doc_total
            return self.total_number_of_named_entities_date_
        
    def total_number_of_named_entities_time(self) -> int:
        """
        returns the number of named entities that are TIME (Times smaller than a day.)
        """
        try:
            return self.total_number_of_named_entities_time_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "TIME")
            self.total_number_of_named_entities_time_ = doc_total
            return self.total_number_of_named_entities_time_
    
    def total_number_of_named_entities_percent(self) -> int:
        """
        returns the number of named entities that are PERCENT (Percentage, including ”%“.)
        """
        try:
            return self.total_number_of_named_entities_percent_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "PERCENT")
            self.total_number_of_named_entities_percent_ = doc_total
            return self.total_number_of_named_entities_percent_
    
    def total_number_of_named_entities_money(self) -> int:
        """
        returns the number of named entities that are MONEY (Monetary values, including unit.)
        """
        try:
            return self.total_number_of_named_entities_money_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "PERCENT")
            self.total_number_of_named_entities_money_ = doc_total
            return self.total_number_of_named_entities_money_
    
    def total_number_of_named_entities_quantity(self) -> int:
        """
        returns the number of named entities that are QUANTITY (Measurements, as of weight or distance.)
        """
        try:
            return self.total_number_of_named_entities_quantity_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "QUANTITY")
            self.total_number_of_named_entities_quantity_ = doc_total
            return self.total_number_of_named_entities_quantity_
    
    def total_number_of_named_entities_ordinal(self) -> int:
        """
        returns the number of named entities that are ORDINAL (“first”, “second”, etc.)
        """
        try:
            return self.total_number_of_named_entities_ordinal_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "ORDINAL")
            self.total_number_of_named_entities_ordinal_ = doc_total
            return self.total_number_of_named_entities_ordinal_
    
    def total_number_of_named_entities_cardinal(self) -> int:
        """
        returns the number of named entities that are CARDINAL (Numerals that do not fall under another type.)
        """
        try:
            return self.total_number_of_named_entities_cardinal_
        except AttributeError:
            doc_total = sum(1 for ent in self.doc.ents if ent.label_ == "CARDINAL")
            self.total_number_of_named_entities_cardinal_ = doc_total
            return self.total_number_of_named_entities_cardinal_