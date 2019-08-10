using System;

namespace Calculator
{
	class Program
	{
		public static void Main(string[] args)
		{
		start:
			{
				Console.WriteLine("Welcome to the Calculator Servant (Press Enter)");
			}
			Console.WriteLine("What is your name? (Please Enter name below and press the Enter Key)");
			string Name = Console.ReadLine();
		start2:
			{
				Console.WriteLine("Thank you " + Name + ". Please enter your first number. (Enter your number and press the Enter Key)");
		}
				string Num1 = Console.ReadLine();
				Console.WriteLine("Ok, " + Num1 + ". What would you like to do? (Please Enter a symbol +,-,*,/)");
				string Operator = Console.ReadLine();
				Console.WriteLine("Ok, " + Operator + ". What's the last number (Please Enter last number of the equation.");
				string Num2 = Console.ReadLine();
				Console.WriteLine("Ok, so it sounds like you would like to do the equation for " + Num1 + Operator + Num2 + ". Is that right? Type Yes or No.");
				string Confirmation = Console.ReadLine();
				if (Confirmation is "no")
				{
					Console.WriteLine("Try again?");
				string GoBackData = Console.ReadLine();
				if (GoBackData is "yes")
				{
					goto start;
				}
				else
				{
					goto end;
				}
			}
			int a = Int32.Parse(Num1);
			int b = Int32.Parse(Num2);
			int c = a * b;
			int d = a / b;
			int e = a + b;
			int f = a - b;
			if (Operator is "*")
			{
				Console.WriteLine("Your Solution is " + c + ".");
			}
			if (Operator is "/")
			{
				Console.WriteLine("Your Solution is " + d + ". ");
			}
			if (Operator is "+")
			{
				Console.WriteLine("Your Solution is " + e + ". ");
			}
			if (Operator is "-")
			{
				Console.WriteLine("Your Solution is " + f + ". ");
			}
			Console.WriteLine("Thanks for using the Calculator Servant. Would you like to do another equation? (Type yes or no.)");
			string FinishData = Console.ReadLine();
				if (FinishData is "yes")
			{
				goto start2;
			}
			else
			{
				goto end;
			}
		end: {
				Console.WriteLine("Thank you for playing.");
					}

		}

	}
}
