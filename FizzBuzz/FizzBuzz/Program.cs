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
                StringBuilder sb = new StringBuilder();

                if (i % 3 == 0)
                {
                    sb.Append("Fizz");
                }
                
                if (i % 5 == 0)
                {
                    sb.Append("Buzz");
                }

                Console.WriteLine(sb.Length == 0 ? i.ToString() : sb.ToString()); 
            } 
            
            Console.Read();
        }
    }
}
