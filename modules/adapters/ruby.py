from __future__ import annotations

from .import util
from .. import dap
from .. import core
from ..settings import Setting

import shutil


class Ruby(dap.AdapterConfiguration):

	type = 'ruby'
	docs = 'https://github.com/castwide/vscode-ruby-debug#debugging-external-programs'

	installer = util.openvsx.OpenVsxInstaller (
		type='ruby',
		repo='wingrunr21/vscode-ruby'
	)

	ruby_readapt = Setting['str|None'] (
		key='ruby_readapt',
		default=None,
		description='Sets a specific path for `readapt` otherwise whatever is in your path will be used'
	)

	async def start(self, log: core.Logger, configuration: dap.ConfigurationExpanded):
		readapt = self.ruby_readapt or shutil.which('readapt')
		if not readapt:
			raise core.Error('You must install the `readapt` gem. Install it by running `gem install readapt` see https://github.com/castwide/vscode-ruby-debug for details.')

		command = [
			readapt,
			'stdio'
		]
		return dap.StdioTransport(log, command)


