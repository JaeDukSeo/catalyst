from collections import OrderedDict

import torch

from catalyst.dl import (
    CheckpointCallback,
    CheckRunCallback,
    ConsoleLogger,
    CriterionCallback,
    ExceptionCallback,
    MetricManagerCallback,
    OptimizerCallback,
    SchedulerCallback,
    TensorboardLogger,
    TimerCallback,
    ValidationManagerCallback,
    VerboseLogger,
)
from catalyst.dl.experiment.supervised import SupervisedExperiment


def _test_callbacks(test_callbacks, exp, stage="train"):
    exp_callbacks = exp.get_callbacks(stage)
    exp_callbacks = OrderedDict(
        sorted(exp_callbacks.items(), key=lambda t: t[0])
    )
    test_callbacks = OrderedDict(
        sorted(test_callbacks.items(), key=lambda t: t[0])
    )

    assert exp_callbacks.keys() == test_callbacks.keys()
    cbs = zip(exp_callbacks.values(), test_callbacks.values())
    for callback, klass in cbs:
        assert isinstance(callback, klass)


def test_defaults():
    """
    Test on defaults for SupervisedExperiment class, which is child class of
    BaseExperiment.  That's why we check only default callbacks functionality
    here
    """
    model = torch.nn.Module()
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    test_callbacks = OrderedDict(
        [
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
        ]
    )

    exp = SupervisedExperiment(model=model, loaders=loaders)
    _test_callbacks(test_callbacks, exp)


def test_defaults_verbose():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_verbose", VerboseLogger),
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
        ]
    )

    model = torch.nn.Module()
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(model=model, loaders=loaders, verbose=True)
    _test_callbacks(test_callbacks, exp)


def test_defaults_check():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_check", CheckRunCallback),
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
        ]
    )

    model = torch.nn.Module()
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(model=model, loaders=loaders, check_run=True)
    _test_callbacks(test_callbacks, exp)


def test_criterion():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
            ("_criterion", CriterionCallback),
        ]
    )

    model = torch.nn.Linear(10, 10)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = None
    scheduler = None
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(
        model=model,
        loaders=loaders,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
    )
    _test_callbacks(test_callbacks, exp)


def test_optimizer():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
            ("_optimizer", OptimizerCallback),
        ]
    )

    model = torch.nn.Linear(10, 10)
    criterion = None
    optimizer = torch.optim.Adam(model.parameters())
    scheduler = None
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(
        model=model,
        loaders=loaders,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
    )
    _test_callbacks(test_callbacks, exp)


def test_scheduler():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
            ("_optimizer", OptimizerCallback),
            ("_scheduler", SchedulerCallback),
        ]
    )

    model = torch.nn.Linear(10, 10)
    optimizer = torch.optim.Adam(model.parameters())
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 10)
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(
        model=model, loaders=loaders, optimizer=optimizer, scheduler=scheduler,
    )
    _test_callbacks(test_callbacks, exp)


def test_all():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_verbose", VerboseLogger),
            ("_check", CheckRunCallback),
            ("_timer", TimerCallback),
            ("_metrics", MetricManagerCallback),
            ("_validation", ValidationManagerCallback),
            ("_saver", CheckpointCallback),
            ("_console", ConsoleLogger),
            ("_tensorboard", TensorboardLogger),
            ("_exception", ExceptionCallback),
            ("_criterion", CriterionCallback),
            ("_optimizer", OptimizerCallback),
            ("_scheduler", SchedulerCallback),
        ]
    )

    model = torch.nn.Linear(10, 10)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 10)
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(
        model=model,
        loaders=loaders,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
        verbose=True,
        check_run=True,
    )
    _test_callbacks(test_callbacks, exp)


def test_infer_defaults():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict([("_exception", ExceptionCallback)])

    model = torch.nn.Linear(10, 10)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 10)
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(
        model=model,
        loaders=loaders,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
    )
    _test_callbacks(test_callbacks, exp, "infer")


def test_infer_all():
    """@TODO: Docs. Contribution is welcome."""
    test_callbacks = OrderedDict(
        [
            ("_verbose", VerboseLogger),
            ("_check", CheckRunCallback),
            ("_exception", ExceptionCallback),
        ]
    )

    model = torch.nn.Linear(10, 10)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 10)
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders["train"] = dataloader

    exp = SupervisedExperiment(
        model=model,
        loaders=loaders,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
        verbose=True,
        check_run=True,
    )
    _test_callbacks(test_callbacks, exp, "infer")
