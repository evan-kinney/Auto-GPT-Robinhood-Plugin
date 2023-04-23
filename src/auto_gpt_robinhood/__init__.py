"""This is a plugin to use Auto-GPT with Robinhood."""
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate

# Robinhood
import pyrh
import os

PromptGenerator = TypeVar("PromptGenerator")

class Message(TypedDict):
    role: str
    content: str


class AutoGPTRobinhoodPlugin(AutoGPTPluginTemplate):
    """
    This is a plugin to use Auto-GPT with Robinhood.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Robinhood"
        self._version = "0.0.1"
        self._description = "This is a plugin for Auto-GPT-Robinhood."
        self.username = os.getenv("ROBINHOOD_USERNAME")
        self.password = os.getenv("ROBINHOOD_PASSWORD")
        self.robinhood = pyrh.Robinhood(self.username, self.password)

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        prompt.add_command(
            "Quote Data",
            "quote_data",
            {
                "symbol": "<symbol>"
            },
            self.quote_data
        ),
        # TODO: get_quote_list
        # TODO: get_quote
        # TODO: get_stock_marketdata
        # TODO: get_historical_quotes
        prompt.add_command(
            "Get Stock News",
            "get_stock_news",
            {
                "symbol": "<symbol>"
            },
            self.get_stock_news
        ),
        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass

    def quote_data(self, stock: str) -> dict:
        """Fetch stock quote.

        Args:
            stock (str or dict): stock ticker symbol or stock instrument

        Returns:
            (:obj:`dict`): JSON contents from `quotes` endpoint

        """
        return self.robinhood.quote_data(stock)

    def get_quote_list(self, stock: str, key: str) -> list:
        """Returns multiple stock info and keys from quote_data (prompt if blank)

        Args:
            stock (str): stock ticker (or tickers separated by a comma)
            , prompt if blank
            key (str): key attributes that the function should return

        Returns:
            (:obj:`list`): Returns values from each stock or empty list
                            if none of the stocks were valid

        """
        return self.robinhood.get_quote_list(stock, key)

    def get_quote(self, stock: str):
        """Wrapper for quote_data."""
        return self.robinhood.get_quote(stock)

    def get_stock_marketdata(self, instruments: list[str]) -> list[dict]:
        """Fetch stock market data.

        Args:
            instruments (list<str>): list of instruments

        Returns:
            (:obj:`list` of :obj:`dict`): List of JSON contents from `marketdata` \
                endpoint, in the same order of input args. If any instrument is \
                invalid, a None will occur at that position.

        """
        return self.robinhood.get_stock_marketdata(instruments)

    def get_historical_quotes(self, stock: str, interval: str, span: str) -> dict:
        """Fetch historical data for stock.

        Note: valid interval/span configs
            interval = 5minute | 10minute + span = day, week
            interval = day + span = year
            interval = week

        Args:
            stock (str): stock ticker
            interval (str): resolution of data
            span (str): length of data
            bounds (:obj:`Bounds`, optional): 'extended' or 'regular' trading hours

        Returns:
            (:obj:`dict`) values returned from `historicals` endpoint

        """
        return self.robinhood.get_historical_quotes(stock, interval, span);

    def get_stock_news(self, stock: str) -> dict:
        """Fetch news endpoint.

        Args:
            stock (str): stock ticker

        Returns:
            (:obj:`dict`) values returned from `news` endpoint

        """
        return self.robinhood.get_news(stock);

    def get_watchlists(self, ) -> dict:
        """Fetch watchlists endpoint and queries for
        each instrumented result aka stock details returned from the watchlist

        Returns:
            (:obj:`dict`): values returned from `watchlists` and `instrument` endpoints
        """
        return self.robinhood.get_watchlists()

    def ask_price(self, stock: str) -> float:
        """Get asking price for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (float): ask price

        """
        return self.robinhood.ask_price(stock)

    def ask_size(self, stock: str) -> int:
        """Get ask size for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (int): ask size

        """
        return self.robinhood.ask_size(stock)

    def bid_price(self, stock: str) -> float:
        """Get bid price for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (float): bid price

        """
        return self.robinhood.bid_price(stock)

    def bid_size(self, stock: str) -> int:
        """Get bid size for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (int): bid size

        """
        return self.robinhood.bid_size(stock)

    def last_trade_price(self, stock: str) -> float:
        """Get last trade price for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (float): last trade price

        """
        return self.robinhood.last_trade_price(stock)

    def previous_close(self, stock: str) -> float:
        """Get previous close price for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (float): previous close price

        """
        return self.robinhood.previous_close(stock)

    def previous_close_date(self, stock: str) -> str:
        """Get previous close date for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (str): previous close date

        """
        return self.robinhood.previous_close_date(stock)

    def get_symbol(self, stock: str) -> str:
        """Get symbol for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (str): symbol

        """
        return self.robinhood.symbol(stock)

    def last_updated_at(self, stock: str) -> str:
        """Get last updated date for a stock.

        Note:
            queries `quote` endpoint, dict wrapper

        Args:
            stock (str): stock ticker

        Returns:
            (str): last updated date

        """
        return self.robinhood.last_updated_at(stock)

    def get_account(self, ) -> dict:
        """Fetch account endpoint.

        Returns:
            (:obj:`dict`) values returned from `account` endpoint

        """
        return self.robinhood.get_account()

    def get_url(self, url: str) -> dict:
        """Fetch url endpoint.

        Args:
            url (str): url to fetch

        Returns:
            (:obj:`dict`) values returned from `url` endpoint

        """
        return self.robinhood.get_url(url)

    def get_tickers_by_tag(self, tag: str) -> list[str]:
        """Fetch tickers by tag.

        Args:
            tag (str): tag to search for

        Returns:
            (:obj:`list` of :obj:`str`) tickers

        """
        return self.robinhood.get_tickers_by_tag(tag)

    def get_options(self, stock: str, expiration_dates: list[str], option_type: str) -> list[dict]:
        """Fetch options for stock.

        Args:
            stock (str): stock ticker
            expiration_dates (list<str>): list of expiration dates
            option_type (str): option type (call or put)

        Returns:
            (:obj:`list` of :obj:`dict`) values returned from `options` endpoint

        """
        return self.robinhood.get_options(stock, expiration_dates, option_type)

    def get_options_owned(self, ) -> list[dict]:
        """Fetch options owned.

        Returns:
            (:obj:`list` of :obj:`dict`) values returned from `options` endpoint

        """
        return self.robinhood.get_options_owned()

    def get_option_market_data(self, option_id: str) -> dict:
        """Fetch option market data.

        Args:
            option_id (str): option id

        Returns:
            (:obj:`dict`) values returned from `option_market_data` endpoint

        """
        return self.robinhood.get_option_market_data(option_id)

    def get_option_chainid(self, symbol: str) -> str:
        """Fetch option chain id.

        Args:
            symbol (str): stock ticker

        Returns:
            (:obj:`str`) option chain id

        """
        return self.robinhood.get_option_chainid(symbol)

    def get_option_quote(self, symbol: str, strike: float, expiration_date: str, option_type: str) -> dict:
        """Fetch option quote.

        Args:
            symbol (str): stock ticker
            strike (float): strike price
            expiration_date (str): expiration date
            option_type (str): option type (call or put)

        Returns:
            (:obj:`dict`) values returned from `option_quote` endpoint

        """
        return self.robinhood.get_option_quote(symbol, strike, expiration_date, option_type)

    def get_fundamentals(self, stock: str) -> dict:
        """Fetch fundamentals.

        Args:
            symbol (str): stock ticker

        Returns:
            (:obj:`dict`) values returned from `fundamentals` endpoint

        """
        return self.robinhood.get_fundamentals(stock)

    def get_portfolio(self, ) -> dict:
        """Fetch portfolio.

        Returns:
            (:obj:`dict`) values returned from `portfolio` endpoint

        """
        return self.robinhood.get_portfolio()

    def order_history() -> list[dict]:
        """Fetch order history.

        Returns:
            (:obj:`list` of :obj:`dict`) values returned from `order_history` endpoint

        """
        return self.robinhood.order_history()

    def get_positions(self, ) -> list[dict]:
        """Fetch positions.

        Returns:
            (:obj:`list` of :obj:`dict`) values returned from `positions` endpoint

        """
        return self.robinhood.get_positions()

    def get_securities_owned(self, ) -> list[dict]:
        """Fetch securities owned.

        Returns:
            (:obj:`list` of :obj:`dict`) values returned from `securities_owned` endpoint

        """
        return self.robinhood.get_securities_owned()

    def place_market_but_order(self, symbol: str, time_in_force: str, quantity: int):
        """Place market buy order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_market_buy_order` endpoint

        """
        return self.robinhood.place_market_buy_order(symbol, time_in_force, quantity)

    def place_limit_buy_order(self, symbol: str, time_in_force: str, quantity: int, price: float):
        """Place limit buy order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            quantity (int): quantity
            price (float): price

        Returns:
            (:obj:`dict`) values returned from `place_limit_buy_order` endpoint

        """
        return self.robinhood.place_limit_buy_order(symbol, time_in_force, quantity, price)

    def place_stop_loss_buy_order(self, symbol: str, time_in_force: str, stop_price: float, quantity: int):
        """Place stop loss buy order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            stop_price (float): stop price
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_stop_loss_buy_order` endpoint

        """
        return self.robinhood.place_stop_loss_buy_order(symbol, time_in_force, stop_price, quantity)

    def place_stop_limit_buy_order(self, symbol: str, time_in_force: str, stop_price: float, price: float, quantity: int):
        """Place stop limit buy order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            stop_price (float): stop price
            price (float): price
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_stop_limit_buy_order` endpoint

        """
        return self.robinhood.place_stop_limit_buy_order(symbol, time_in_force, stop_price, price, quantity)

    def place_market_sell_order(self, symbol: str, time_in_force: str, quantity: int):
        """Place market sell order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_market_sell_order` endpoint

        """
        return self.robinhood.place_market_sell_order(symbol, time_in_force, quantity)

    def place_limit_sell_order(self, symbol: str, time_in_force: str, price: float, quantity: int):
        """Place limit sell order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            price (float): price
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_limit_sell_order` endpoint

        """
        return self.robinhood.place_limit_sell_order(symbol, time_in_force, price, quantity)

    def place_stop_loss_sell_order(self, symbol: str, time_in_force: str, stop_price: float, quantity: int): 
        """Place stop loss sell order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            stop_price (float): stop price
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_stop_loss_sell_order` endpoint

        """
        return self.robinhood.place_stop_loss_sell_order(symbol, time_in_force, stop_price, quantity)

    def place_stop_limit_sell_order(self, symbol: str, time_in_force: str, price: float, stop_price: float, quantity: int):
        """Place stop limit sell order.

        Args:
            symbol (str): stock ticker
            time_in_force (str): 'GFD' or 'GTC' (day or until cancelled)
            price (float): price
            stop_price (float): stop price
            quantity (int): quantity

        Returns:
            (:obj:`dict`) values returned from `place_stop_limit_sell_order` endpoint

        """
        return self.robinhood.place_stop_limit_sell_order(symbol, time_in_force, price, stop_price, quantity)

    def get_open_orders(self, ) -> list[dict]:
        """Fetch open orders.

        Returns:
            (:obj:`list` of :obj:`dict`) values returned from `open_orders` endpoint

        """
        return self.robinhood.get_open_orders()

    def cancel_order(order_id: str):
        """Cancel order.

        Args:
            order_id (str): order id

        Returns:
            (:obj:`dict`) values returned from `cancel_order` endpoint

        """
        return self.robinhood.cancel_order(order_id)