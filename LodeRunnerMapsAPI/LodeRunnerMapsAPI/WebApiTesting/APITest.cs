using LodeRunnerMapsAPI.Controllers;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Threading.Tasks;
using System.Web.Http.Results;

namespace WebApiTesting
{
    [TestClass]
    public class APITest
    {
        readonly string ScriptPath = "D:/LastYear/Licenta/LodeRunnerMachineLearning/generate/main.py";
        [TestMethod]
        public void Run_Cmd_Should_Return_Complete_Map()
        {
            var mapsController = new MapsController();
            var result = mapsController.Run_cmd(ScriptPath,"");
            Assert.AreEqual(result.Length, 448);
        }
        [TestMethod]
        public void Level_Should_Return_Complete_Map()
        {
            var mapsController = new MapsController();
            var actionResult = mapsController.Level();
            var result = actionResult as OkNegotiatedContentResult<string>;
            Assert.AreEqual(result.Content.Length, 448);
        }
    }
}
