"""!

@brief Integration-tests for Hierarchical Sync (HSyncNet) algorithm.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2020
@license BSD-3-Clause

"""


import unittest;

import matplotlib;
matplotlib.use('Agg');

from pyclustering.cluster.tests.hsyncnet_templates import HsyncnetTestTemplates;

from pyclustering.nnet import solve_type;

from pyclustering.samples.definitions import SIMPLE_SAMPLES;

from pyclustering.core.tests import remove_library;


class HsyncnetIntegrationTest(unittest.TestCase):
    def testClusteringSampleSimple1WithoutCollectingByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, [5, 5], solve_type.FAST, 5, 0.3, False, True);
    
    def testClusteringSampleSimple1ByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, [5, 5], solve_type.FAST, 5, 0.3, True, True);
         
    def testClusteringOneAllocationSampleSimple1ByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, [10], solve_type.FAST, 5, 0.3, True, True);

    def testClusteringSampleSimple2ByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 3, [10, 5, 8], solve_type.FAST, 5, 0.2, True, True);

    def testClusteringOneAllocationSampleSimple2ByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, [23], solve_type.FAST, 5, 0.2, True, True);

    def testClusteringOneDimensionDataSampleSimple7ByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE7, 2, [10, 10], solve_type.FAST, 5, 0.3, True, True);

    def testClusteringTheSameData1ByCore(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE12, 3, [5, 5, 5], solve_type.FAST, 5, 0.3, True, True);

    def testDynamicLengthCollectingByCore(self):
        HsyncnetTestTemplates.templateDynamicLength(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, None, 5, 0.3, True, True);

    def testDynamicLengthWithoutCollectingByCore(self):
        HsyncnetTestTemplates.templateDynamicLength(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, None, 5, 0.3, False, True);


    @remove_library
    def testProcessingWhenLibraryCoreCorrupted(self):
        HsyncnetTestTemplates.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, [5, 5], solve_type.FAST, 5, 0.3, False, True);
