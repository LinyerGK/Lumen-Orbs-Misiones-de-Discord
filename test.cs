using System;
using System.Windows.Forms;
class Program { 
    static void Main(string[] args) { 
        var f = new Form(); 
        f.Text = args.Length > 0 ? string.Join(" ", args) : "Game"; 
        f.Width = 350; f.Height = 150;
        f.FormBorderStyle = FormBorderStyle.FixedDialog;
        f.MaximizeBox = false;
        f.StartPosition = FormStartPosition.CenterScreen;
        var lbl = new Label() { Text = "Lumen Orbs Simulation Running...\nDo not close this window.", AutoSize = true, Location = new System.Drawing.Point(50, 40) };
        f.Controls.Add(lbl);
        Application.Run(f); 
    } 
}
