from discord import option 

from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    

    @commands.slash_command(name="add", name_localization={"ru": "сложение"}, description="Add two numbers", description_localizations={"ru": "Сложение двух чисел"})
    @option(name="first", name_localizations={"ru": "первое"}, description="first number", description_localizations={"ru": "Первое число выражения"})
    @option(name="second", name_localizations={"ru": "второе"}, description="second number", description_localizations={"ru": "Второе число выражения"})
    async def add(self, ctx, first: int, second: int):
        result = first + second
        await ctx.respond(f"Если к числу {first} прибавить число {second}, будет {result}.")


    @commands.slash_command(name="substract", name_localization={"ru": "вычитание"}, description="Substruction of two numbers", description_locaizations={"ru": "Вычитание двух чисел"})
    @option(name="first", name_localizations={"ru": "первое"}, description="first number", description_localizations={"ru": "Первое число выражения"})
    @option(name="second", name_localizations={"ru": "второе"}, description="second number", description_localizations={"ru": "Второе число выражения"})
    async def substract(self, ctx, first: int, second: int):
        result = first - second
        await ctx.respond(f"Если из числа {first} вычесть число {second}, будет {result}.")


    @commands.slash_command(name="mult", name_localization={"ru": "умножение"}, description="Multiplication of two numbers", description_locaizations={"ru": "Умножение двух чисел"})
    @option(name="first", name_localizations={"ru": "первое"}, description="first number", description_localizations={"ru": "Первое число выражения"})
    @option(name="second", name_localizations={"ru": "второе"}, description="second number", description_localizations={"ru": "Второе число выражения"})
    async def mult(self, ctx, first: int, second: int):
        result = first * second
        await ctx.respond(f"Если число {first} умножить на число {second}, будет {result}.")


    @commands.slash_command(name="divivte", name_localization={"ru": "деление"}, description="Division of two numbers", description_localization={"ru": "Деление двух чисел"})
    @option(name="first", name_localizations={"ru": "первое"}, description="first number", description_localizations={"ru": "Первое число выражения"})
    @option(name="second", name_localizations={"ru": "второе"}, description="second number", description_localizations={"ru": "Второе число выражения"})
    async def divide(self, ctx, first: int, second: int):
        result = first / second
        await ctx.respond(f"Если число {first} поделить на число {second}, будет {result}.")
        