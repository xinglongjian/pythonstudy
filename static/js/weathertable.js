var oTable;
var TableEditable = function () {

    var handleTable = function (url,cityid,date) {
        if(oTable)
         {
           oTable.fnClearTable(false);
           oTable.fnDestroy();
         }
        oTable = $('#weather_table').dataTable({

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
            "sAjaxSource":url+"?cityid="+cityid+"&date="+date,
            
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
            }
           
        });

    }

    return {

        //main function to initiate the module
        init: function (url,productId,pubdir) {
            handleTable(url,productId,pubdir);
        }

    };

}();