pragma solidity ^0.4.25;

contract EscrowBase {
	
	event NewEscrow(uint creatorId, string type_name);

	uint16 _commissionAmount;

	struct escrowType {
		string name;
		string description;
		uint256 expirationTimeInSeconds = 600;
	}
	escrowType[] public escrowTypes;
	
	struct escrowStatus {
		string name;
	}

	struct transactionType {
		string name;
		string description;
	}


	struct Escrow {
		uint escrowId;
		uint escrowCreator;
		string title;
		uint escrowTypeId;
		string expirationDate;
		uint escrowAmount;
		uint statusId;
	}

	Escrow[] public escrowAgreements;

	# to be used by the creator and cosigner
	mapping (address => uint) public signersOnEscrow;

	function _

	function _generateEscrowId(string _str) private view returns (uint) {
		uint eid = uint(keccak256(abi.encodePacked(_str)));
		return eid;
	}

	function _createEscrow(address _address, string _title, uint _typeId) {}

}