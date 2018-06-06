using System;
using System.Diagnostics;
using System.IO;
using System.Net.Http;
using System.Web.Http;

namespace LodeRunnerMapsAPI.Controllers
{
    public class MapsController : ApiController
    {
        [HttpGet]
        public IHttpActionResult Level()
        {
            var result = run_cmd("D:/LastYear/Licenta/LodeRunnerMachineLearning/generate/main.py", "");
            return Ok(result);
        }
        private string run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "C:/Users/silvi/AppData/Local/conda/conda/envs/LodeRunner/python.exe";
            start.Arguments = string.Format("{0} {1}", cmd, args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    return result;
                }
            }
        }
    }
}
