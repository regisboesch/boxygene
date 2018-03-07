<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class AddForeignKeysToSubscriptionsTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::table('subscriptions', function(Blueprint $table)
		{
			$table->foreign('contact_id', 'fk_subscriptions_1')->references('id')->on('contacts')->onUpdate('NO ACTION')->onDelete('NO ACTION');
			$table->foreign('subscription_status_id', 'fk_subscriptions_2')->references('id')->on('subscription_statuses')->onUpdate('NO ACTION')->onDelete('NO ACTION');
		});
	}


	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		Schema::table('subscriptions', function(Blueprint $table)
		{
			$table->dropForeign('fk_subscriptions_1');
			$table->dropForeign('fk_subscriptions_2');
		});
	}

}
