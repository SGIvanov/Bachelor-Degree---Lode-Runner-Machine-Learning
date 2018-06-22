using System.Diagnostics;
using System.IO;
using System.Web.Http;

namespace LodeRunnerMapsAPI.Controllers
{
    public class MapsController : ApiController
    {
        [HttpGet]
        public IHttpActionResult Level()
        {
            var result = Run_cmd("D:/LastYear/Licenta/LodeRunnerMachineLearning/generate/main.py", "");
            return Ok(result);
        }
        public string Run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo
            {
                FileName = "C:/Users/silvi/AppData/Local/conda/conda/envs/LodeRunner/python.exe",
                Arguments = string.Format("{0} {1}", cmd, args),
                UseShellExecute = false,
                RedirectStandardOutput = true
            };
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    return "Test";
                }
            }
        }
    }
}





