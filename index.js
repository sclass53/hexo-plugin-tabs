/**
 * Main program
 * Windows distribution
 * Version: 0.0.1 DEV
 * Language: 
 *      - js
 *      - python
 * Tools:
 *      - Node.js
 */


var wconsolelog=console.log;

console.log=function(_temp){}

var fs = require('fs');
var path = require('path');
var exec = require('child_process').exec;

// Folder Path for the _posts- editable
var EDITABLE_POSTFOLDER="\\source\\_posts\\";

//Paths
var filePath = path.resolve('');

//default-generator
var generatorpath="node_modules\\hexo-plugin-tabs\\bin\\dist\\sa.exe"


filePath=filePath+EDITABLE_POSTFOLDER;

//Python runner

function excecpy(gp,pathq){
    var cmdStr = gp+' '+pathq;
    //Run the exe program
    exec(cmdStr,function(err,stdout,stderr){if(err) {
            wconsolelog('exec error: '+stderr);
        }else{
            wconsolelog(stdout);
        }
    });
}

// fs reader
//wconsolelog(filePath);

/**
 * @param filePath
 * 
 */
function _dost(){
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
                            excecpy(generatorpath,filedir);
                        }else{
                            ;
                        }
                    }
                })
            });
        }
    });
}



//Main

hexo.extend.filter.register('before_generate', function(){
    //ban output

    //Disable output
    console.log=function(_temp){}
    _dost();
    //var postslist=require("./bin/get_posts");
    wconsolelog("plugin-tabs: Tab generated successfully");
    //excecpy("hexo","g")
  });

/**
 * END
 */