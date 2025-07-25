/** No-op base class for Jasmine reporters.
 *
 * @constructor
 */
//jasmine.Reporter = function() {
package org.jasmineflex
{
	public dynamic class Reporter
	{
		jasmine.Reporter = Reporter;
		
		//noinspection JSUnusedLocalSymbols
		jasmine.Reporter.prototype.reportRunnerStarting = function(runner) {
		};
		
		//noinspection JSUnusedLocalSymbols
		jasmine.Reporter.prototype.reportRunnerResults = function(runner) {
		};
		
		//noinspection JSUnusedLocalSymbols
		jasmine.Reporter.prototype.reportSuiteResults = function(suite) {
		};
		
		//noinspection JSUnusedLocalSymbols
		jasmine.Reporter.prototype.reportSpecStarting = function(spec) {
		};
		
		//noinspection JSUnusedLocalSymbols
		jasmine.Reporter.prototype.reportSpecResults = function(spec) {
		};
		
		//noinspection JSUnusedLocalSymbols
		jasmine.Reporter.prototype.log = function(str) {
		};
	}
}