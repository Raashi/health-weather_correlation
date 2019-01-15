from science.classes import Sample, Standard
from science.reports import MulSamplesStandard, MulSamplesMulStandards

from logic import QFrameBase
from frames.std_mul_samples import Ui_FrameStdMulSamples
from frames.mul_std_mul_samples import Ui_FrameMulStdMulSamples
from logic.group import QFrameGroup


class QFrameStdMulSamples(QFrameBase, Ui_FrameStdMulSamples):
    def __init__(self, parent, std):
        QFrameBase.__init__(self, parent, Ui_FrameStdMulSamples)

        layout = self.layout()

        values = list(Sample.samples.keys())
        values.remove(Sample.group.name)
        self.frame_group = QFrameGroup(self, values)
        self.frame_group.signal_func = self.group_changed
        layout.insertWidget(0, self.frame_group)

        self.std = Standard.standards[std]
        self.report = None

        self.group_changed(self.frame_group.get_turned())

    def group_changed(self, new_values):
        self.report = MulSamplesStandard([Sample.samples[name] for name in new_values], self.std)
        self.title_label.setText("Эталон: {}. {} значений".format(self.std.name, len(new_values)))


class QFrameMulStdMulSamples(QFrameBase, Ui_FrameMulStdMulSamples):
    def __init__(self, parent):
        QFrameBase.__init__(self, parent, Ui_FrameMulStdMulSamples)

        layout = self.layout()

        stds = list(Standard.standards.keys())
        samples = list(Sample.samples.keys())
        samples.remove(Sample.group.name)

        self.frame_group_stds = QFrameGroup(self, stds)
        self.frame_group_stds.signal_func = self.group_stds_changed
        layout.insertWidget(0, self.frame_group_stds)

        self.frame_group_samples = QFrameGroup(self, samples)
        self.frame_group_samples.signal_func = self.group_samples_chanhed
        layout.insertWidget(1, self.frame_group_samples)

        self.report = None
        self.update(stds, samples)

    def group_stds_changed(self, new_stds):
        self.update(new_stds, self.frame_group_samples.get_turned())

    def group_samples_chanhed(self, new_samples):
        self.update(self.frame_group_stds.get_turned(), new_samples)

    def update(self, new_stds, new_samples):
        self.title_label.setText("{} эталонов, {} образцов".format(len(new_stds), len(new_samples)))
        # self.report = MulSamplesMulStandards([Sample.samples[sample_name] for sample_name in new_samples],
        #                                      [Standard.standards[std_name] for std_name in new_stds])
