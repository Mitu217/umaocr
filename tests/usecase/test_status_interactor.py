import asyncio
import csv
import logging
import os
from unittest import TestCase

from PIL import Image

import resources
from app.domain.parameters import SupportParameters
from app.driver.file_driver import LocalFileDriverImpl
from app.usecase.status_interactor import StatusInteractor


class TestSkillInteractor(TestCase):
    def test_get_support_parameters_from_image(self) -> None:
        for image_name, result_name in (
            ('normal1.jpg', 'normal1.csv'),
            ('normal2.jpg', 'normal2.csv'),
            ('normal3.png', 'normal3.csv'),
            ('normal4.png', 'normal4.csv'),
            ('normal5.png', 'normal5.csv'),
            ('normal6.png', 'normal6.csv'),
            ('normal7.png', 'normal7.csv'),
            ('normal8.png', 'normal8.csv'),
        ):
            with self.subTest(image_name=image_name):
                status_interactor = StatusInteractor(
                    LocalFileDriverImpl(''),
                    logging.getLogger(__name__),
                )

                with Image.open(
                        os.path.join(resources.__path__[0], 'tests',
                                     'support_character_modal_aoharu', image_name)) as image:
                    got = asyncio.run(status_interactor.get_support_parameters_from_image(image))

                with open(
                        os.path.join(resources.__path__[0], 'tests',
                                     'support_character_modal_aoharu', result_name)) as result:
                    wants = []
                    reader = csv.reader(result)
                    for row in reader:
                        wants.append(
                            SupportParameters(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[5]),
                                int(row[6]),
                                int(row[7]),
                                int(row[8]),
                                int(row[9]),
                                int(row[10]),
                            )
                        )
                    want = wants[0]

                self.assertEqual(got, want)
