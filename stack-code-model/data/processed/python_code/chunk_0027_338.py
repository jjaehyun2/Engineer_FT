/**
 * Created by christoferdutz on 02.08.16.
 */
package org.dukecon.services {
import mx.collections.ArrayCollection;
import mx.collections.Sort;
import mx.collections.SortField;

import org.dukecon.model.ConferenceStorage;

public class StreamService {

    [Inject]
    public var conferenceService:ConferenceService;

    public function StreamService() {
    }

    public function getStreams(conferenceId:String):ArrayCollection {
        var conference:ConferenceStorage = conferenceService.getConference(conferenceId);
        if(conference) {
            var res:ArrayCollection = conference.conference.metaData.tracks;

            // Sort the locations by order.
            var orderSortField:SortField = new SortField();
            orderSortField.name = "order";
            orderSortField.numeric = true;
            var locationSort:Sort = new Sort();
            locationSort.fields = [orderSortField];
            res.sort = locationSort;
            res.refresh();

            return res;
        }

        return null;
    }

}
}