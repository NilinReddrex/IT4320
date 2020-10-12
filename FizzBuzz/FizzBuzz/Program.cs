using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i = 1; i <= 100; i++)
            {
                string output = string.Empty;

                if (i % 3 == 0)
                {
                    output += "Fizz";
                }
                
                if(i % 5 == 0)
                {
                    output += "Buzz";
                }

                Console.WriteLine(output == string.Empty ? i.ToString() : output); 
            } 
            
            Console.Read();
        }
    }
}
