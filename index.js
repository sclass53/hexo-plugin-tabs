var wconsolelog=console.log;
console.log=function(qq){}
var fs = require('fs');
var path = require('path');
var exec = require('child_process').exec;
function excecpy(pathq){
    var cmdStr = 'python ./node_modules/hexo-plugin-tabs/bin/sa.py '+pathq;
    exec(cmdStr,function(err,stdout,stderr){if(err) {
            wconsolelog('python exec error'+stderr);

        }else{

            wconsolelog(stdout);

        }

    });
}

//解析需要遍历的文件夹，我这以E盘根目录为例
var filePath = path.resolve('');
filePath=filePath+"\\source\\_posts\\"
//wconsolelog(filePath);

/**
 * @param filePath
 * 
 */
fs.readdir(filePath,function(err,files){
    if(err){
        console.warn(err)
    }else{
        //遍历读取到的文件列表
        files.forEach(function(filename){
            //获取当前文件的绝对路径
            var filedir = path.join(filePath,filename);
            //根据文件路径获取文件信息，返回一个fs.Stats对象
            fs.stat(filedir,function(eror,stats){
                if(eror){
                    console.warn('获取文件stats失败');
                }else{
                    var isFile = stats.isFile();//是文件
                    var isDir = stats.isDirectory();//是文件夹
                    if(isFile){
                        //wconsolelog(filedir);
                        excecpy(filedir);
                    }else{
                        ;
                    }
                }
            })
        });
    }
});


hexo.extend.filter.register('before_generate', function(){
    console.log("plugin-tabs: Tab generated successfully");
    //ban output
    console.log=function(qq){}
    //var postslist=require("./bin/get_posts");
    //wconsolelog(postslist);
  });
