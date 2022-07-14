class listOpenOnly_topK(Resource):
    def get(self):
        topK = int(flask.request.args.get('top'))
        _items = db.controlPoints.find().limit(topK)
        ret_val = []
        for obj in _items:
            km = "control point @ " + str(obj['km']) + " km"
            open_time = "open date/time: " + obj['open_time_field']
            ret_val.append(km)
            ret_val.append(open_time)
        return { 'Laptops': ret_val }


class listCloseOnly_topK(Resource):
    def get(self):
        _items = db.controlPoints.find()
        _items_sorted = sorted(_items, key=attrgetter('km'))

        #.limit(topK)
        ret_val = []
        try:
            topK = int(flask.request.args.get('top'))
            for obj in _items_sorted[:topK]:
                km = "control point @ " + str(obj['km']) + " km"
                close_time = "close date/time: " + obj['close_time_field']
                ret_val.append(km)
                ret_val.append(close_time)
        except:
            for obj in _items_sorted:
                km = "control point @ " + str(obj['km']) + " km"
                close_time = "close date/time: " + obj['close_time_field']
                ret_val.append(km)
                ret_val.append(close_time)
        return { 'Laptops': ret_val }


api.add_resource(listOpenOnly_topK, '/listOpenOnly/json?top=<int:id>')
api.add_resource(listCloseOnly_topK, '/listCloseOnly/json?top=<int:id>')
