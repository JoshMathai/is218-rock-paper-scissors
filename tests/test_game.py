"""Unit tests for the Rock, Paper, Scissors winner rules."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
def test_rock_against_rock_is_tie():
    """Matching rock moves tie."""
    assert determine_winner("rock", "rock") == "tie"


@pytest.mark.unit
def test_rock_against_paper_is_loss():
    """Paper covers rock, so the player loses."""
    assert determine_winner("rock", "paper") == "lose"


@pytest.mark.unit
def test_rock_against_scissors_is_win():
    """Rock crushes scissors, so the player wins."""
    assert determine_winner("rock", "scissors") == "win"


@pytest.mark.unit
def test_paper_against_rock_is_win():
    """Paper covers rock, so the player wins."""
    assert determine_winner("paper", "rock") == "win"


@pytest.mark.unit
def test_paper_against_paper_is_tie():
    """Matching paper moves tie."""
    assert determine_winner("paper", "paper") == "tie"


@pytest.mark.unit
def test_paper_against_scissors_is_loss():
    """Scissors cut paper, so the player loses."""
    assert determine_winner("paper", "scissors") == "lose"


@pytest.mark.unit
def test_scissors_against_rock_is_loss():
    """Rock crushes scissors, so the player loses."""
    assert determine_winner("scissors", "rock") == "lose"


@pytest.mark.unit
def test_scissors_against_paper_is_win():
    """Scissors cut paper, so the player wins."""
    assert determine_winner("scissors", "paper") == "win"


@pytest.mark.unit
def test_scissors_against_scissors_is_tie():
    """Matching scissors moves tie."""
    assert determine_winner("scissors", "scissors") == "tie"


@pytest.mark.integration
def test_real_post_shows_rock_loses_to_paper(monkeypatch):
    """A real Flask request applies the rules and displays the loss."""
    web.app.config.update(TESTING=True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    response = web.app.test_client().post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "You chose" in page and "Rock" in page
    assert "Computer chose" in page and "Paper" in page
    assert 'data-outcome="lose"' in page
    assert "Computer wins" in page
    assert "game rules not built yet" not in page
