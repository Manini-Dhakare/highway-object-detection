import math


class EuclideanDistTracker:
    def __init__(self):
        # Store object center positions
        self.center_points = {}

        # Store missing frames for each object
        self.disappeared = {}

        # ID counter
        self.id_count = 0

        # Distance threshold
        self.max_distance = 70

        # Maximum frames object can disappear
        self.max_missing = 10


    def update(self, objects_rect):

        objects_bbs_ids = []

        # If no objects detected
        if len(objects_rect) == 0:
            for id in list(self.disappeared.keys()):
                self.disappeared[id] += 1

                if self.disappeared[id] > self.max_missing:
                    del self.center_points[id]
                    del self.disappeared[id]

            return objects_bbs_ids


        new_center_points = {}

        for rect in objects_rect:

            x, y, w, h = rect

            cx = int(x + w / 2)
            cy = int(y + h / 2)

            same_object = False


            for id, pt in self.center_points.items():

                distance = math.hypot(cx - pt[0], cy - pt[1])


                if distance < self.max_distance:

                    new_center_points[id] = (cx, cy)
                    self.disappeared[id] = 0

                    objects_bbs_ids.append(
                        [x, y, w, h, id]
                    )

                    same_object = True
                    break


            if same_object == False:

                new_center_points[self.id_count] = (cx, cy)
                self.disappeared[self.id_count] = 0

                objects_bbs_ids.append(
                    [x, y, w, h, self.id_count]
                )

                self.id_count += 1


        # Update centers
        for id in list(self.center_points.keys()):
            if id not in new_center_points:
                self.disappeared[id] += 1

                if self.disappeared[id] <= self.max_missing:
                    new_center_points[id] = self.center_points[id]
                else:
                    del self.disappeared[id]


        self.center_points = new_center_points.copy()

        return objects_bbs_ids