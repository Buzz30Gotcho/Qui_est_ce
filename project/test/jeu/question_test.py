import pytest
from project.src.jeu.Question import Question

class TestQuestion: 
    def test_instanciation_classe_abstraite(self):
        with pytest.raises(NotImplementedError):
            Question()
            