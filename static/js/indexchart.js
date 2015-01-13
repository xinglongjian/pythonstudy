
/**
 *当天各个时间点的温度 
 */
function currechartInit(city_id,url,disturl)
   {
    var urlOpEchartData=url;
    $.getJSON(urlOpEchartData,{id:city_id},function(json){
         require.config({
            paths: {
                echarts: disturl
            }
         });
         require(
         [
            'echarts',
            'echarts/chart/line'
         ],
         function (ec) {
             var myChart = ec.init(document.getElementById('todayEchart'),'shine');
             var option = {
                title:{
                    text:'各城市当天温度'
                },
                tooltip : {
                    trigger: 'axis',
                    axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                        type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                legend: {
                    data:json.legend
                },
                toolbox: {
                    show : false,
                    feature : {
                       mark : {show: true},
                       dataView : {show: true, readOnly: false},
                       magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                       restore : {show: true},
                       saveAsImage : {show: true}
                    }
                },
                calculable : true,
                xAxis : [
                 {
                    type : 'category',
                    boundaryGap : false,
                    data : json.keys
                 }
                 ],
                yAxis : [
                 {
                   type : 'value',
                   axisLabel : {
                      formatter: '{value} °C'
                   }
                 }
                ],
                series : [
                 {
                   name:json.legend[0],
                   type:'line',
                   stack: '总量',
                   itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
                   data:json.values
                 }
                 ]
             };
              myChart.setOption(option);
           }
         );
    });
}

/**
 * 各城市每周的最高气温和最低气温
 */
function weekeChartInit(city_id,url,disturl)
{
    var urlOpEchartData=url;
    $.getJSON(urlOpEchartData,{id:city_id},function(json){
         require.config({
            paths: {
                echarts: disturl
            }
         });
         require(
         [
            'echarts',
            'echarts/chart/line'
         ],
         function (ec) {
             var myChart = ec.init(document.getElementById('weekEchart'),'shine');
             var option = {
                title:{
                    text:'过去7天的HL温度'
                },
                tooltip : {
                    trigger: 'axis',
                    axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                        type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                legend: {
                    data:['最高气温','最低气温']
                },
                toolbox: {
                    show : false,
                    feature : {
                       mark : {show: true},
                       dataView : {show: true, readOnly: false},
                       magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                       restore : {show: true},
                       saveAsImage : {show: true}
                    }
                },
                calculable : true,
                xAxis : [
                 {
                    type : 'category',
                    boundaryGap : false,
                    data : json.keys
                 }
                 ],
                yAxis : [
                 {
                   type : 'value',
                   axisLabel : {
                     formatter: '{value} °C'
                   }
                 }
                ],
                series : [
                 {
                   name:'最高气温',
                   type:'line',
                   data:json.htemps,
                   markPoint : {
                     data : [
                        {type : 'max', name: '最大值'},
                        {type : 'min', name: '最小值'}
                     ]
                   },
                   markLine : {
                     data : [
                        {type : 'average', name: '平均值'}
                     ]
                   }
                 },
                 {
                   name:'最低气温',
                   type:'line',
                   data:json.ltemps,
                   markPoint : {
                     data : [
                       {type : 'max', name: '最大值'},
                       {type : 'min', name: '最小值'}
                     ]
                   },
                  markLine : {
                    data : [
                       {type : 'average', name : '平均值'}
                    ]
                  }
                 }
                 ]
             };
              myChart.setOption(option);
           }
         );
    });
}
/**
 * 各城市选择某天的最高气温和最低气温进行聚类分析
 */
function clusterChartInit(url,disturl)
{
    var urlOpEchartData=url;
    $.getJSON(urlOpEchartData,function(json){
         require.config({
            paths: {
                echarts: disturl
            }
         });
         require(
         [
            'echarts',
            'echarts/chart/scatter'
         ],
         function (ec) {
             var myChart = ec.init(document.getElementById('clusterEchart'),'shine');
             var option = {
                title:{
                    text:'KMeans聚类分析'
                },
                tooltip : {
                    trigger: 'axis',
                    showDelay : 0,
                    axisPointer:{
                       type : 'cross',
                       lineStyle: {
                          type : 'dashed',
                          width : 1
                       }
                    }
                },
                legend: {
                    data:['南方城市','北方城市']
                },
                toolbox: {
                    show : false,
                    feature : {
                       mark : {show: true},
                       dataZoom : {show: true},
                       dataView : {show: true, readOnly: false},
                       restore : {show: true},
                       saveAsImage : {show: true}
                    }
                },
                xAxis : [
                 {
                    type : 'value',
                    name:'最高温度',
                    scale:true,
                    axisLabel : {
                        formatter: '{value} °C'
                    }
                 }
                 ],
                yAxis : [
                 {
                   type : 'value',
                   name:'最低温度',
                   scale:true,
                   axisLabel : {
                     formatter: '{value} °C'
                   }
                 }
                ],
                series : [
                 {
                   name:'南方城市',
                   type:'scatter',
                   data:json.ltemps
                   //data:[[ 9 , 3],[ 9,  6],[13 , 6],[13 , 3],[13 , 5], [11,  6],[13,  5],[12,  9],[14, 10],[13 ,9]],
                 },
                 {
                   name:'北方城市',
                   type:'scatter',
                   data:json.htemps
                   //data:[[4,-4],[5,-2],[5,-5],[2,-3],[6,-3],[6,-3],[7, 0],[6, -2]],
                 }
                 ]
             };
              myChart.setOption(option);
           }
         );
    });
}