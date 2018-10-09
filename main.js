const {app, BrowserWindow} = require('electron')

function createWindow () {
  window = new BrowserWindow({width: 800, height: 600})
  window.loadFile('index.html')

  /* var python = require('child_process').spawn('python', ['./hello.py']);
  python.stdout.on('data',function(data){
        console.log("data: ",data.toString('utf8'));
  }); */

  var pyshell = require('python-shell')
  var path = require('path')

  var options = {
    mode: 'text',
    pythonPath: '/anaconda3/lib/python3.6',
    scriptPath: path.join(__dirname),
    args: ['invoicefile']
  }

  pyshell.run('app/routes.py', function (err, results) {
    if (err) console.log(err)
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
