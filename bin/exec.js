var ww=console.log;
var exec = require('child_process').exec;
function excecpy(pathq){
    var cmdStr = 'python sa.py';
    exec(cmdStr,function(err,stdout,stderr){if(err) {
            ww('python exec error'+stderr);

        }else{/*这个stdout的内容就是上面我curl出来的这个东西：*/

            ww(stdout);

        }

    });
}
module.exports = excecpy;