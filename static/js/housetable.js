var oTable;
var HouseEditable = function () {

    var handleTable = function (url,bzid,commid,room,liveroom,orien,area,price,sortcolumn,sorttype,purl) {
        if(oTable)
         {
           oTable.fnClearTable(false);
           oTable.fnDestroy();
         }
        oTable = $('#house_table').dataTable({

            "lengthMenu": [
                [10, 30, 100, -1],
                [10, 30, 100, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 10,
            "bProcessing": true,
            "bServerSide": true,
            "bAutoWidth":true,
            "bFilter":false,
            "bSort":false,
            "sServerMethod": "get",
            "sAjaxSource":url+"?bzid="+bzid+"&commid="+commid+"&room="+room+"&liveroom="+liveroom+"&orien="+orien+"&area="+area+"&price="+price+
                         "&sortcolumn="+sortcolumn+"&sorttype="+sorttype,
            
            "sEmptyTable":"表中数据为空",
            "pagingType": "full_numbers",
            "oLanguage": {
                "sLengthMenu": "显示 _MENU_ 项结果",
                "oPaginate": {
                	"sFirst":"<<",
                	"sLast":">>",
                    "sPrevious": "<",
                    "sNext": ">"
                },
                "sEmptyTable":"无结果",
                "sProcessing":"处理中...",
                "sLoadingRecords":"加载中...",
                "sInfoEmpty":"显示第 0 至 0 项结果，共 0 项",
                "sInfo":"显示第 _START_ 至 _END_ 项结果, 共 _TOTAL_ 项."
            },
             "columnDefs": [ 
                           {
                             "render": function (data, type, row) {
                                   return '<a href="javascript:showHousePrice(\''+purl+'\',\''+data+'\')">'+data+'</a>';
                              },
                               "targets": [1]
                           }]
           
        });

    }

    return {

        //main function to initiate the module
        init: function (url,bzid,commid,room,liveroom,orien,area,price,sortcolumn,sorttype,purl) {
            handleTable(url,bzid,commid,room,liveroom,orien,area,price,sortcolumn,sorttype,purl);
        }

    };

}();

function showHousePrice(url,houseCode)
{
    var urlOpEchartData=url;
    $.getJSON(urlOpEchartData,{housecode:houseCode},function(json){
         require.config({
            paths: {
                echarts: '/static/plugins/echarts/dist'
            }
         });
         require(
         [
            'echarts',
            'echarts/chart/line'
         ],
         function (ec) {
             var myChart = ec.init(document.getElementById('houseEchart'),'shine');
             var option = {
                title:{
                    text:'价格变化趋势'
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
                      formatter: '{value}万'
                   }
                 }
                ],
                series : [
                 {
                   name:json.legend[0],
                   type:'line',
                   stack: '价格',
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