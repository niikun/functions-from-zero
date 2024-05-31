from click.testing import CliRunner
from mylib.bot import scrape
from wikibot import cli


def test_scrape():
    assert "Microsoft" in scrape("Microsoft",1)


def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--word','OpenAI'])
    assert result.exit_code == 0
    assert result.output == 'OpenAI is an American artificial intelligence (AI) research organization founded in December 2015, researching artificial intelligence with the goal of developing "safe and beneficial" artificial general intelligence, which it defines as "highly autonomous systems that outperform humans at most economically valuable work." As one of the leading organizations of the AI boom, it has developed several large language models, advanced image generation models, and previously, released open-source models.\n'
