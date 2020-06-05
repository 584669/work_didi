select
    count(*)
from
(
    select
        param,
        row_number() over (partition by param['order_id'] order by param['timestamp'] desc) rank
    from gulfstream_ods.ods_log_g_driverecosys_feeinterceptor
    where concat(year,month,day) between '20200525' and '20200525'
    and param ['order_id'] is not null
    and param ['order_id'] != 0
    and param['navi_trip_event_type_count_xgb'] > 0
    and param['normal_distance_xgb']>=3000
    and param['normal_distance_xgb']-param['navi_trip_first_driver_show_eda']>2000
    and param['is_modify_dest']=0
    and param['p_total_fee - pre_total_fee']>0
    and param['combo_type']!=4
)q where q.rank = 1;
