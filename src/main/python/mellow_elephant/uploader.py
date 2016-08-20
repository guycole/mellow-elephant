#
# Title:uploader.py
# Description:uploader
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os

class Uploader:


    def writeObservations(self, dataDirectory, sortie, observationUrl):
        uploadObservation = UploadObservation()

        targets = os.listdir(sortie.getDirectory(dataDirectory))
        for target in targets:
            if target.startswith('observation'):
                fileName = sortie.getDirectory(dataDirectory) + "/" + target
                print fileName
                observation = pickle.load(open(fileName, "rb"))

#                flag = uploadObservation.execute(observation, sortie, observationUrl)
#                if flag:
#                    os.remove(fileName)
#                else:
#                    print 'observation upload failure'
#                    return


class UploadObservation:

    def upload(self, observationList, sortie, observationUrl):
        """
        perform upload
        """
        message = {}
        message['installationId'] = sortie.installationId
        message['sortieId'] = sortie.sortieId
        message['observationList'] = observationList

        payload = json.dumps(message)

        headers = {'Accept':'application/json', 'Content-Type':'application/json;charset=UTF-8'}

        request = urllib2.Request(observationUrl, payload, headers)

        try:
            response = urllib2.urlopen(request, timeout=22)
            result = json.loads(response.read())
            response.close()

            if result['status'] == 'OK':
                return True
        except urllib2.HTTPError:
                print 'UploadSortie exception:' + observationUrl

        return False

    def execute(self, observations, sortie, observationUrl):
        """
        upload observation
        """
        result = False
        counter = 0
        observationList = []
        for item in observations:
            observationList.append(item.toDictionary())

#            if counter > 100:
#                result = self.upload(observationList, sortie, observationUrl)
#                if result:
#                    counter = 0
#                    observationList = []
#                else:
#                    print 'observation upload failure noted'
#                    return result
#            else:
#                counter += 1

#        if len(observationList) > 0:
#            result = self.upload(observationList, sortie, observationUrl)

        return result


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
