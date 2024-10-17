import project
from art import text2art


ascii_art = text2art("THE END", font="bubble")
test_output = "\n".join([f"\t\t\t\t{line}" for line in ascii_art.split("\n")])


def test_random_authors():
    line = "There was an Old Man in a tree,"
    assert project.poem_by_line(line) == test_output
    assert project.poem_by_line("qwerty") == "Poem Not Found"


def test_poem_by_linecount():
    assert project.poem_by_linecount("5") == test_output
    assert project.poem_by_linecount(10) == test_output
    assert project.poem_by_linecount("qwerty") == "Poem Not Found"
    assert project.poem_by_linecount(0) == "Poem Not Found"


def test_poem_by_author():
    assert project.poem_by_author("Charlotte Smith") == test_output
    assert project.poem_by_author("William Shakespeare") == test_output
    assert project.poem_by_author("abc") == "Author Not Found"


def test_poem_by_title():
    assert project.poem_by_title("Tears") == test_output
    assert project.poem_by_title("Summer Sun") == test_output
    assert project.poem_by_title("abcdefgh") == "Title Not Found"
