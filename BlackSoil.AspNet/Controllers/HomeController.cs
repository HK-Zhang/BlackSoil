using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using BlackSoil.AspNet.Models;
using System.Data.SqlClient;

namespace BlackSoil.AspNet.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            string CONN = "Data Source=sqlservice,1433;Initial Catalog=snoopyshoppingcart;Persist Security Info=True;User ID=sa;Password=Password1234;";

            string msg = "Your contact page.";

            try
            {
                using (var connection = new SqlConnection(CONN))
                {
                    var command = new SqlCommand("SELECT top (1) * FROM shopping", connection);
                    connection.Open();
                    using (var reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            var record = new
                            {
                                AddedOn = Convert.ToDateTime(reader["AddedOn"]),
                                ConnectionID = reader["ConnectionID"].ToString(),
                                IP = reader["IP"].ToString(),
                                CartItem = reader["CartItem"].ToString()
                            };

                            msg = $"IP:{record.IP}, CartItem:{record.CartItem}, AddedOn:{record.AddedOn}";
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                throw ex;
            }


            ViewData["Message"] = msg;

            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
