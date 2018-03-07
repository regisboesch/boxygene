<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class AddForeignKeysToSubscriptionItemsTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::table('subscription_items', function(Blueprint $table)
		{
			$table->foreign('subscription_id', 'fk_subscription_items_1')->references('id')->on('subscriptions')->onUpdate('NO ACTION')->onDelete('NO ACTION');
		});
	}


	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		Schema::table('subscription_items', function(Blueprint $table)
		{
			$table->dropForeign('fk_subscription_items_1');
		});
	}

}
